#!/usr/bin/python3

"""
This module sends a request to a given URL,
and displays the value of the variable
X-Request-Id in the response header.
"""

import requests
import sys


def main():
    # Check that the script is called with one argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        return

    # Send a request to the given URL and get the response header
    response = requests.get(sys.argv[1])
    headers = response.headers

    # Check if the X-Request-Id header is present in the response
    if "X-Request-Id" in headers:
        x_request_id = headers.get("X-Request-Id")
        print(f"The X-Request-Id is: {x_request_id}")
    else:
        print("The X-Request-Id header is not present in the response.")


if __name__ == "__main__":
    main()
