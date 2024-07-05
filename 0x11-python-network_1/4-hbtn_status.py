#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status
using requests
"""
if __name__ == "__main__":
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
