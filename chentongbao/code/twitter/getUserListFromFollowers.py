from tweepy import OAuthHandler
from tweepy import API
from collections import Counter
from datetime import datetime, date, time, timedelta
import sys
import json
import os
import io
import re
import time
import tweepy

'''
https://labsblog.f-secure.com/2018/02/27/how-to-get-twitter-follower-data-using-python-and-tweepy/
'''
if sys.version_info[0] >= 3:
    unicode = str

# Helper functions to load and save intermediate steps
def save_json(variable, filename):
    with io.open(filename, "w", encoding="utf-8") as f:
        f.write(unicode(json.dumps(variable, indent=4, ensure_ascii=False)))


def load_json(filename):
    ret = None
    if os.path.exists(filename):
        try:
            with io.open(filename, "r", encoding="utf-8") as f:
                ret = json.load(f)
        except:
            pass
    return ret


def try_load_or_process(filename, processor_fn, function_arg):
    load_fn = None
    save_fn = None
    if filename.endswith("json"):
        load_fn = load_json
        save_fn = save_json
    else:
        load_fn = load_bin
        save_fn = save_bin
    if os.path.exists(filename):
        print("Loading " + filename)
        # print(">>>>>>" + load_fn(filename))
        ret = load_fn(filename)  # 文件不存在时，调用get_follower_ids获取user的followers列表
        print("Saving " + filename)
        '''当处理的新用户的followers为0时，返回none会导致save_fn(ret + processor_fn(function_arg), filename)
TypeError: can only concatenate list (not "NoneType") to list'''
        temp = processor_fn(function_arg)
        if temp != "skip" and temp and isinstance(temp,list):
        # if processor_fn(function_arg):
            #两个list合并并去重
            save_fn(list(set(ret + processor_fn(function_arg))), filename)
        else:
            save_fn(ret, filename)
        return load_fn(filename)    #文件存在时，直接返回已经存在的json文件
        # print (">>>>>>"+load_fn(filename))
    else:
        ret = processor_fn(function_arg)
        print("Saving " + filename)
        save_fn(ret, filename)
        return ret


# Some helper functions to convert between different time formats and perform date calculations
def twitter_time_to_object(time_string):
    twitter_format = "%a %b %d %H:%M:%S %Y"
    match_expression = "^(.+)\s(\+[0-9][0-9][0-9][0-9])\s([0-9][0-9][0-9][0-9])$"
    match = re.search(match_expression, time_string)
    if match is not None:
        first_bit = match.group(1)
        second_bit = match.group(2)
        last_bit = match.group(3)
        new_string = first_bit + " " + last_bit
        date_object = datetime.strptime(new_string, twitter_format)
        return date_object


def time_object_to_unix(time_object):
    return int(time_object.strftime("%m"))
    # return int(time_object.strftime("%H").strip("'"))

    # return int(time_object.strftime("%H (0-23) or %I (0-11)"))


def twitter_time_to_unix(time_string):
    return time_object_to_unix(twitter_time_to_object(time_string))


def seconds_since_twitter_time(time_string):
    input_time_unix = int(twitter_time_to_unix(time_string))
    current_time_unix = int(get_utc_unix_time())
    return current_time_unix - input_time_unix


def get_utc_unix_time():
    dts = datetime.utcnow()
    return time.mktime(dts.timetuple())


# Get a list of follower ids for the target account
def get_follower_ids(target):
    try:
        return auth_api.followers_ids(target)
    except tweepy.TweepError:
        # return "none"
        print("Failed to run the command on that user, Skipping...")
        return "skip"
    finally:
        print('in finally')
        # pass
    '''
    https://www.cnblogs.com/windlazio/archive/2013/01/24/2874417.html
    https://zhuanlan.zhihu.com/p/26094540
    http://www.cnblogs.com/JohnABC/p/4065437.html
    '''



# Twitter API allows us to batch query 100 accounts at a time
# So we'll create batches of 100 follower ids and gather Twitter User objects for each batch
def get_user_objects(follower_ids):
    batch_len = 100
    num_batches = len(follower_ids) / 100
    batches = (follower_ids[i:i + batch_len] for i in range(0, len(follower_ids), batch_len))
    all_data = []
    for batch_count, batch in enumerate(batches):
        sys.stdout.write("\r")
        sys.stdout.flush()
        sys.stdout.write("Fetching batch: " + str(batch_count) + "/" + str(num_batches))
        sys.stdout.flush()
        users_list = auth_api.lookup_users(user_ids=batch)
        users_json = (map(lambda t: t._json, users_list))
        all_data += users_json
    return all_data


# Creates one week length ranges and finds items that fit into those range boundaries
def make_ranges(user_data, num_ranges=20):
    range_max = 604800 * num_ranges
    range_step = range_max / num_ranges

    # We create ranges and labels first and then iterate these when going through the whole list
    # of user data, to speed things up
    ranges = {}
    labels = {}
    for x in range(num_ranges):
        start_range = x * range_step
        end_range = x * range_step + range_step
        label = "%02d" % x + " - " + "%02d" % (x + 1) + " weeks"
        labels[label] = []
        ranges[label] = {}
        ranges[label]["start"] = start_range
        ranges[label]["end"] = end_range
    for user in user_data:
        if "created_at" in user:
            account_age = seconds_since_twitter_time(user["created_at"])
            # for label, timestamps in ranges.iteritems():
            for label, timestamps in ranges.items():

                if account_age > timestamps["start"] and account_age < timestamps["end"]:
                    entry = {}
                    id_str = user["id_str"]
                    entry[id_str] = {}
                    fields = ["screen_name", "name", "created_at", "friends_count", "followers_count",
                              "favourites_count", "statuses_count"]
                    for f in fields:
                        if f in user:
                            entry[id_str][f] = user[f]
                    labels[label].append(entry)
    return labels

if __name__ == "__main__":
    # account_list = ["9715012","13393052"]   [9715012,13393052]
    account_list = load_json("follower_ids.json")
    # account_list.append(9715012)
    if len(account_list) <= 10000000 :
        '''
        if (len(sys.argv) > 1):
            account_list = sys.argv[1:]

        if len(account_list) < 1:
            print("No parameters supplied. Exiting.")
            sys.exit(0)
'''
        '''
        you should set your own param here.# consumer_key consumer_secret access_token  access_token_secret#
        '''
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        '''
        https://stackoverflow.com/questions/38775997/getting-this-error-when-using-tweepy
        you just reached the Twitter Streaming API limit. It takes about one hour to let you extract tweets again.
        You should add the wait_on_rate_limit=True option when initializing tweetpy :
        '''
        auth_api = API(auth,wait_on_rate_limit=True)
        visited_list = []
        for target in account_list:
            if target not in visited_list:
                visited_list.append(target)
                # print("Processing target: " + target)

                # Get a list of Twitter ids for followers of target account and save it获取目标用户的followers_id号以及对应id的基本信息并保存
                filename = "follower_ids.json"
                # if get_follower_ids(target) != "none":

                # if temp != "skip" and temp and isinstance(temp,list):
                follower_ids = try_load_or_process(filename, get_follower_ids, target)
            # else:
            #     pass
