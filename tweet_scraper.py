import json
import tweepy
import csv
import time

def getTweets(fromm, too):
#TWITTER AUTH
    """
    Here we would have the following four variables, but due to security concerns,
    we have had to remove them from the public version of the project:

    - CONSUMER_KEY
    - CONSUMER_SECRET
    - ACCESS_TOKEN
    - ACCESS_TOKEN_SECRET
    """

    authtweet = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    authtweet.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(authtweet)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    # NOTE: "meatball" refers to the data environment with the Twitter API
    return api.search_full_archive("meatball", "#thebachelorette", fromDate = fromm, toDate = too, maxResults = 100)

def processTweets(statusList):
    tdlist = []
    for z in statusList:
        temp = []
        temp.append(z.id)
        temp.append(z.text)
        temp.append(z.user)
        temp.append(z.retweet_count)
        temp.append(z.lang)
        temp.append(z.created_at)
        tdlist.append(temp)
    write_to_csv(tdlist)

# List of dates corresponding to episodes from Wikipedia scrape
timeperiod = [
"05-27-13",
"06-03-13",
"06-10-13",
"06-17-13",
"06-24-13",
"07-01-13",
"07-08-13",
"07-15-13",
"07-22-13",
"07-29-13",
"08-05-13",
"08-05-13",
"05-19-14",
"05-26-14",
"06-01-14",
"06-02-14",
"06-09-14",
"06-16-14",
"06-23-14",
"06-30-14",
"07-07-14",
"07-14-14",
"07-21-14",
"07-28-14",
"07-28-14",
"05-18-15",
"05-19-15",
"05-25-15",
"06-01-15",
"06-08-15",
"06-15-15",
"06-22-15",
"06-29-15",
"07-06-15",
"07-13-15",
"07-20-15",
"07-27-15",
"07-27-15",
"05-23-16",
"05-30-16",
"06-06-16",
"06-07-16",
"06-20-16",
"06-27-16",
"07-11-16",
"07-18-16",
"07-25-16",
"07-26-16",
"08-01-16",
"08-01-16",
"05-22-17",
"05-29-17",
"06-05-17",
"06-19-17",
"06-26-17",
"06-27-17",
"07-10-17",
"07-17-17",
"07-24-17",
"07-31-17",
"08-07-17",
"05-28-18",
"06-04-18",
"06-11-18",
"06-18-18",
"06-25-18",
"07-02-18",
"07-09-18",
"07-16-18",
"07-23-18",
"07-30-18",
"08-06-18",
"05-13-19",
"05-20-19",
"05-27-19",
"06-03-19",
"06-11-19",
"06-17-19",
"06-24-19",
"07-01-19",
"07-08-19",
"07-15-19",
"07-22-19",
"07-29-19",
"07-30-19",
"10-13-20",
"10-20-20",
"10-27-20",
"11-05-20",
"11-10-20",
"11-17-20",
"11-24-20",
"12-01-20",
"12-08-20",
"12-14-20",
"12-15-20",
"12-21-20",
"12-22-20",
"06-07-21",
"06-14-21",
"06-21-21",
"06-28-21",
"07-05-21",
"07-12-21",
"07-19-21",
"07-26-21",
"08-02-21",
"08-09-21",
"10-19-21",
"10-26-21",
"11-02-21",
"11-09-21",
"11-16-21",
"11-23-21",
"11-30-21",
"12-06-21",
"12-14-21"]

def write_to_csv(Even_list):
     with open('/Users/<USERNAME>/Desktop/tweetrealdata.csv', 'a', newline='') as csvfile:
         writer = csv.writer(csvfile)
         writer.writerows(Even_list)

def date_list_to_time(datelist):
    timelist2 = ["0100"]
    UTClist = []
    for entry in datelist:
        temp = entry.split("-")
        entry3 = str("20" + temp[2])+str(temp[0])+str(temp[1])
        for entry2 in timelist2:
            UTClist.append(entry3 + entry2)
    return UTClist


adjusteddatelist = date_list_to_time(timeperiod)
adjusteddatelist.append("MEATBALL")
for entry in range(len(adjusteddatelist)):
    if( adjusteddatelist[entry + 1] == "MEATBALL"):
        break
    try:
        tweetlist = getTweets(adjusteddatelist[entry],adjusteddatelist[entry + 1])
    except:
        print("unable to get tweets from " + adjusteddatelist[entry]+ ", " + adjusteddatelist[entry + 1])
    processTweets(tweetlist)

    time.sleep(30)
