# 10/25/2025

import json

data = {"name": "Saeed", "age": 15, "skills": ["Python", "OOP"]}

# Save to json file
with open("data.json", "w") as file:
    json.dump(data, file)

# Load from json file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)