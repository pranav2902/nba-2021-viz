import pandas as pd
import numpy as np
import praw
import requests
import json
import csv
import time
import datetime
#Using Requests
def getPushshiftData(query,before,after,sub):
  url = 'https://api.pushshift.io/reddit/search/submission/?title='+str(query)+'&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
  print(url)
  with requests.get(url,stream=True) as r:
    data = json.loads(r.text)
  return data['data']


## Function to collect important post data
def collectSubmData(subm):
  submdata = []
  sub_id = subm["id"]
  title = subm["title"]
  linkfull = subm["full_link"]
  score = subm["score"]
  created = datetime.datetime.fromtimestamp(subm['created_utc'])
  numcomments = subm["num_comments"]
  submdata.append((sub_id,title,linkfull,score,created,numcomments))
  substats[sub_id] = submdata




## Function to convert the Json data to a CSV file and store it
def toCsvFile():
    count = 0
    location = "C:\\Users\\Pranav\\nba 2021 viz\\playerRedditData\\"
    filename = query + ".csv"
    file = location + filename
    with open(file, 'w', newline='', encoding='utf-8') as file: 
        a = csv.writer(file, delimiter=',')
        headers = ["Post ID","Title","Link","Score","Publish Date","Total No. of Comments"]
        a.writerow(headers)
        for sub in substats:
            a.writerow(substats[sub][0])
            count+=1
            
        print(str(count) + " submissions have been uploaded")
    file.close()

## Function to show top 5 posts

# Main
if __name__ == "__main__":
  ## Chosen Before and After times from Start of 20-21 regular season to end of Playoffs
  after = "1608575400"
  before = "1626892200"
  sub = "nba"
  substats = {}
  #Input name of player/team/event
  print("Enter Name of Player/Event/Team")
  query = input()
  subcount = 0

  ## Loop for reinitializing after parameter, to get over Pushshift api's limit of 100 posts in every call

  data = getPushshiftData(query, before, after, sub)
  while(len(data)>0):
    for submission in data:
      collectSubmData(submission)
      subcount += 1
    print(len(data))
    print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    after = data[-1]['created_utc']
    data = getPushshiftData(query, before,after, sub)
  print(len(data))


  print(str(len(substats)) + " submissions have added to list")
  print("1st entry is:")
  print(list(substats.values())[0][0][1] + " created: " + str(list(substats.values())[0][0][4]))
  print("Last entry is:")
  print(list(substats.values())[-1][0][1] + " created: " + str(list(substats.values())[-1][0][4]))
  toCsvFile()

  