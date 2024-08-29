class Mashina:
    def __init__(self, brand, model):
        self.brand_ = brand
        self.model_ = model

    def move(self):
        print(self.brand_,"  ", self.model_)

class Car(Mashina):
    def move(self):
        print("Car ",self.brand_,"  ", self.model_)


class Boat(Mashina):
    pass


class Plane(Mashina):
    def __init__(self, brand, model):
        super().__init__(brand, model)



car1 = Car("Ford", "Mustang")  # Create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  # Create a Plane class

for x in (car1, boat1, plane1):
    x.move()

