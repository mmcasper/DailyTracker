import json

dictionary = {
    "name" : "mmcasper",
    id : 1,
}

#serializing json
username_dict = json.dumps(dictionary, indent=2)

#writing to data.py
with open("username_dict", "w") as outfile:
    outfile.write(username_dict)

print(username_dict)