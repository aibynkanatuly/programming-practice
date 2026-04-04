# json.py

import json

# Python dictionary
data = {
    "name": "Aibyn",
    "age": 18,
    "city": "Almaty"
}

# Convert Python to JSON
json_string = json.dumps(data, indent=4)
print("JSON string:")
print(json_string)

# Write JSON to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded from file:")
print(loaded_data)

# Parse JSON string
parsed = json.loads(json_string)
print("Parsed name:", parsed["name"])