#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using
the requests package and displays the body of the response in
a specified format.
"""

import requests


def fetch_status(url):
    """
    Fetches the content from the specified URL and prints the response body.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        None
    """
    try:
        response = requests.get(url)
        response_text = response.text
        print("Body response:")
        print("\t- type:", type(response_text))
        print("\t- content:", response_text)
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_status(url)
