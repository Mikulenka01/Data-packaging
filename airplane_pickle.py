import pickle


class Airplane:
    def __init__(self, model, airline, capacity):
        self.model = model
        self.airline = airline
        self.capacity = capacity

    def fly(self):
        print(f"{self.model} is flying.")

    def land(self):
        print(f"{self.model} has landed.")

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
            print(f"{self.model} data serialized to {filename}")

    @staticmethod
    def deserialize(filename):
        with open(filename, 'rb') as file:
            airplane = pickle.load(file)
            print(f"{airplane.model} data deserialized from {filename}")
            return airplane


airplane = Airplane("Boeing 747", "Air Example", 416)

airplane.serialize('airplane.pkl')

new_airplane = Airplane.deserialize('airplane.pkl')
new_airplane.fly()

