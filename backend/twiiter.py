import twint
import os
import re
import json
import yaml
from config import tweetpath
from deep_translator import GoogleTranslator
from functions import json_format


# pyyaml==5.4.1


def twint_scrapper(hashtags, project_id=0, k=0, is_video=False):
    for i in hashtags:
        i2 = re.sub("#", "", i)
        c = twint.Config()
        c.Search = i2
        c.Lang = "en"
        c.Limit = 100
        #c.Min_likes = 1
        c.Output = os.path.join(
            tweetpath, "tweet_non_processed/non_processed.json")
        k = k+1
        c.Filter_retweets = True
        c.Store_json = True
        c.Hide_output = True
        twint.run.Search(c)
        print(f"Scrapped for Hashtags = {k}" + f" - {i2}")

    # scrapping done & preprocessing start
    json_format(os.path.join(tweetpath, "tweet_non_processed/non_processed.json"),
                os.path.join(tweetpath, "tweet_processed/out.json"))
    os.remove(os.path.join(tweetpath, "tweet_non_processed/non_processed.json"))

    os.rename(os.path.join(tweetpath, "tweet_processed/out.json"),
              os.path.join(tweetpath, f"tweet_processed/project_{project_id}.json"))
    print("Scrapping Completed")

    data = yaml.load(open(os.path.join(
        tweetpath, f"tweet_processed/project_{project_id}.json"), 'r', encoding='utf-8'))
    with open(os.path.join(tweetpath, f"tweet_processed/project_{project_id}_final.json"), 'w') as f:
        json.dump(data, f)

    with open(os.path.join(tweetpath, f"tweet_processed/project_{project_id}_final.json"), 'r', encoding='utf-8') as f:
        json_content = json.loads(f.read())

    return json_content['data']


def g_translation_function_en(inText):
    try:
        if len(inText) <= 4999:
            outText = GoogleTranslator(
                source='auto', target='en').translate(inText)
            return outText
        else:
            return inText
    except Exception as e:
        print(e)
        return inText


def ranker(data, param=0.5):
    for tweet in data:
        try:
            if sentence_prediction(tweet['tweet']) > param:
                tweet['prediction'] = 1
            else:
                tweet['prediction'] = 0
        except Exception as e:
            print(e)
            tweet['prediction'] = 0
    return data
