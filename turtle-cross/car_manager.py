from car import Car
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance= random.randint(1,6)
        if random_chance == 1:
            color = random.choice(COLORS)
            random_y = random.randint(-240, 240)

            car = Car(color, random_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move(STARTING_MOVE_DISTANCE)
