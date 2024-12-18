import pickle


class MyObject:
    def __init__(self, text):
        self.text = text

    def __reduce__(self):
        return (print, (self.text,))


# Vytvoření instance MyObject
obj = MyObject("Hello, world!")

# Serializace objektu
pickled_obj = pickle.dumps(obj)

# Deserializace objektu, což spustí funkci print
pickle.loads(pickled_obj)
