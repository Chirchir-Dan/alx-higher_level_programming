#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL,
and displays the value of the X-Request-Id header found in the response.
"""

import sys
import requests


def get_request_id(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Check if the 'X-Request-Id' header is present
            if 'X-Request-Id' in response.headers:
                request_id = response.headers['X-Request-Id']
                print(request_id)
            else:
                print("No X-Request-Id header found in the response.")
        else:
            print(f"Failed to retrieve data, status code:\
                    {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_request_id(url)
