from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.up()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            y_cor = random.randint(-220, 220)
            new_car.goto((300, y_cor))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def detect_collision(self, person):
        for car in self.all_cars:
            if car.distance(person) < 20:
                return True
        return False

    def level_up(self):
        self.car_speed += MOVE_INCREMENT