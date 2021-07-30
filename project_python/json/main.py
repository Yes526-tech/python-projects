# deserialize
import json

# with open("person.json") as file:
#     #    data = file.read()
#     data = json.load(file)
# print(data["first_name"])

data = """
    {
  "first_name": "Yunus",
  "last_name": "Sert",
  "hobbies": [
    "basketball",
    "programming"
  ],
  "age": 16,
  "siblings": [
    {
      "first_name": "esra",
      "age": 13
    },
    {
      "first_name": "Kadir",
      "age": 6
    }
  ]
}
"""
data = json.loads(data)
print(data)
print(type(data))