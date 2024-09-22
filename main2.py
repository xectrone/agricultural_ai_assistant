import json
with open('disease_description.json', encoding='utf8') as JSONFile:
    data = json.load(JSONFile)
for i in data:
    print(i)

print(len(data))

