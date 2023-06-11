import json

# Assuming the JSON data is stored in a file named 'data.json'
with open('iptv.json') as json_file:
    data = json.load(json_file)

# Accessing the link inside the JSON
link = data['url']

print(link)  # Output: https://manusoft.github.io/api/scorpio/v1/
