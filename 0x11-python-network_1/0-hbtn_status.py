#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status using urllib
and displays the body of the response.
"""

import urllib.request

def fetch_status(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_status(url)
