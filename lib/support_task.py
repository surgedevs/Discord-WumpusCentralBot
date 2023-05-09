"""
:author @DzikStar
:contributors @DzikStar

This library is storing all custom stuff and functions used for Discord Support Tracker
Including some requests stuff, comparing between two stored RSS and etc

Used in:
  - ./main.py
"""

import requests
import utils.worker_logs # Unused

GITHUB_RSS = 'https://raw.githubusercontent.com/Wumpus-Central/databases/main/discord-support.rss?token='
GITLAB_RSS = 'https://gitlab.com/derpystuff/discord-support/-/commits/main?format=atom'


# @Surge: I'm guessing the parameter is a string? Need clarification.
def import_all_files(ghp_atoken: str) -> None:
    """
    This function is used to import all files from GitHub and GitLab to our repository

    :param ghp_atoken: str
    :return: None
    """

    response_old_rss = requests.get(GITHUB_RSS + ghp_atoken)
    if response_old_rss.status_code == 200:
        print()  # worker_logs
    else:
        print()  # worker_logs
    response_new_rss = requests.get(GITLAB_RSS)
    if response_new_rss.status_code == 200:
        print()  # worker_logs
    else:
        print()  # worker_logs
