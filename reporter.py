from os import error, link
import feedparser
import datetime
import re
import sqlite3
from colorama import Fore, Back, Style, init
def ScreenStarter():
  init(autoreset=True)
  print("############################################################################\n")
  print("+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+")
  print(Fore.RED +"|C|y|b|e|r| |S|e|c|u|r|i|t|y| |N|e|w|s|")
  print("+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+")
  print("\n############################ Author : Ali Haydar TOPRAK ####################")

x = datetime.datetime.now()

N_Year = int(x.year)
N_Mon = int(x.month)
N_Day = int(x.day)

def cleanhtml(Sum):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', Sum)
  cleanr = re.compile('&#.*?;')
  cleantextt = re.sub(cleanr, '', cleantext)
  return cleantextt

def AllFeeds():

    with open("sources.txt") as file:
        while (line := file.readline().rstrip()):
            SiteUrl = line
            NewsFeed = feedparser.parse(SiteUrl)
            feedcounts = len(NewsFeed.entries)
            for i in range(0,feedcounts):
                entry = NewsFeed.entries[i]
                try:
                    P_Year = int(entry["published_parsed"][0])
                    P_Mon = int(entry["published_parsed"][1])
                    P_Day = int(entry["published_parsed"][2])

                    if N_Year == P_Year and N_Mon == P_Mon and N_Day == P_Day:
                        Title = entry["title"]
                        Sum = entry["summary"]
                        Sum = cleanhtml(Sum)
                        Link = entry["link"]
                        Publish = entry["published"]
                        print("\n")                 
                        print("-"*200)
                        print("Title : {}\nSummary : {}\nLink : {}\nDate : {}\nSource : {}".format(Title,Sum,Link,Publish,SiteUrl))
                        print("-"*200)
                        
                except:
                    continue

if __name__ == "__main__":
    ScreenStarter()
    AllFeeds()
