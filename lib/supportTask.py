## Author: @DzikStar
## Contributors: @DzikStar
##
## Description:
## This library is stroing all custom stuff and functions used for Discord Support Tracker 
## Including some requests stuff, comparing between two stored RSS and etc
##
## Used in:
##   - ./main.py

import requests
import feedparser
import ## there should be workerLogs from utils

githubRSS = str('https://raw.githubusercontent.com/Wumpus-Central/databases/main/discord-support.rss?token=')
gitlabRSS = str('https://gitlab.com/derpystuff/discord-support/-/commits/main?format=atom')

def importAllFiles(GHPAtoken):
    ## This fuction is used to import all files from GitHub and GitLab to our repository
    ## Imported Variables:
    ##   - GHPAtoken = Token user for our database repository (required if we wanna download RSS-xml raw) 

    responseOldRSS = requests.get(githubRSS+GHPAtoken)
    if responseOldRSS.status_code == 200:
        print() ## place for workerLogs
    else:
        print() ## place for workerLogs
    responseNewRSS = requests.get(gitlabRSS)
    if responseNewRSS.status_code == 200:
        print() ## place for workerLogs
    else:
        print() ## place for workerLogs