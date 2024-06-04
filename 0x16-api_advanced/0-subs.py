#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys  

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Feisty_Taste_9498)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

if __name__ == "__main__":  # Added to handle script execution from command-line
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("Number of subscribers:", number_of_subscribers(subreddit))

