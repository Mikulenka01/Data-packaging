import json

print("Hello JSON")

data = {"name": "John",
        "age": 25,
        "kids": [],
        "married": False}


"""j_data = json.dumps(data)
print(j_data)
print(data)
print(type(j_data))
print(type(data))
new_data = json.loads(j_data)
print(new_data)
print(type(new_data))"""

class Person:
    def __init__(self, name, age, married):
        self.name = name
        self.age = age
        self.married = married

    def __str__(self):
        return f"{self.name} is {self.age} years old"


p = Person("John", 25, False)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


with open('data.json', 'r') as infile:
    data = json.load(infile)
    print(data)
    print(type(data))