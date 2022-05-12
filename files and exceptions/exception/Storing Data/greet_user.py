################## not solve ####### page- 204
import json
filename = "totocompany.json"
with open(filename) as f:
    username = json.load(f)
    print(f"welcome back, {username}!")