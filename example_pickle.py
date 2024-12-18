import json
import pickle


class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def save_to_json(self, name):
        data = {
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'color': self.color
        }
        with open(f'{name}.json', 'w') as outfile:
            json.dump(data, outfile)


    @staticmethod
    def from_json(file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)

        return Car(data['brand'], data['model'], data['year'], data['color'])


    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.color}'

    def start(self):
        print("I am starting.")



cars = [Car("bmw", "X6", 2020, "black"),
        Car("audi", "X6", 2020, "black"),
        Car("Skoda", "octavia", 2020, "black")]

data = pickle.dumps(cars)
print(data)
new_data = pickle.loads(data)
print(new_data)

with open('cars.pkl', 'wb') as handle:
    pickle.dump(cars, handle)

with open('cars.pkl', 'rb') as handle:
    cars = pickle.load(handle)
print(cars)