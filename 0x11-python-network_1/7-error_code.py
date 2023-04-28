#!/usr/bin/python3

"""
This module sends a GET request to a given URL,
displays the body of the response, and prints an error message
if the HTTP status code is greater than or equal to 400.
"""

import requests
import sys


def main():
    # Check that the script is called with one argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        return

    # Send a GET request to the URL
    url = sys.argv[1]
    response = requests.get(url)

    # If the HTTP status code is greater than or equal to 400,
    # print an error message
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Otherwise, display the body of the response
        print(response.text)


if __name__ == "__main__":
    main()
