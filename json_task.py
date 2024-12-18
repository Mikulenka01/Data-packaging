import json


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

counter = 0
for c in cars:
    c.save_to_json(f"car{counter}")
    print(c.__dict__)
    counter += 1

cars_data = [c.__dict__ for c in cars]

json.dump(cars_data, open('cars.json', 'w'))


new_car = Car.from_json("car0.json")
new_car.start()