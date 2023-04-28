#!/usr/bin/python3
"""A script that takes your Github credentials,
- (Username and password)
- uses the GithHub API to display your ID
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = 'https://api.github.com/user'
response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    user_data = response.json()
    print(f"User ID: {user_data['id']}")
else:
    print(f"Error: {response.status_code} - {response.reason}")
