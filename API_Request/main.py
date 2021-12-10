import requests
import os
import json

username = "sgv1984@gmail.com"
token = os.environ.get("GITHUB_TOKEN")

r = requests.get("https://api.github.com/user/repos", 
                 auth=(username, token))
#print(json.dumps(r.json(), indent=4))

for repo in r.json():
    print(f"Repo name: {repo['name']}\n Repo URL: {repo['html_url']}\n")