#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password) and uses
   the GitHub API to display your id
"""

import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    headers = {
                   "Accept": "application/vnd.github+json",
                   "Authorization": "Bearer {}".format(sys.argv[2])
              }
    with requests.get(url, headers=headers) as response:
        print(response.json().get('id'))
