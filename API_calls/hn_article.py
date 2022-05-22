import requests
import json

# Make an Ap
url = 'https://hacker-news.firebaseio.com/v0/items/19155826.json'
r = requests.get(url)
print(f"Status code : {r.status_code}")

# Explore
response_dict = r.json()
readable_file = r'C:\Users\User\PycharmProjects\data_visualization\API_calls\data\readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)