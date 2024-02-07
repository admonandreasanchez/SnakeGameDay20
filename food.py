from turtle import Turtle
import random
import time
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("teal")
        self.speed("fastest")
        self.is_special = False
        self.special_food_timer = None
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

        # Si la comida actual no es especial, asegúrate de que se mueva a una nueva ubicación
        if not self.is_special:
            self.goto(random_x, random_y)

    def special_food(self):
        self.is_special = True
        self.shape('square')
        self.color("red")
        random_x_special_food = random.randint(-280, 280)
        random_y_special_food = random.randint(-280, 280)
        self.goto(random_x_special_food, random_y_special_food)
        self.special_food_start_time = time.time()
    def reset_special_food(self):
        self.is_special = False
        self.shape('circle')  # Cambia el shape de nuevo a "circle"
        self.color("teal")  # Cambia el color de nuevo a "teal"
        self.goto(1000, 1000)  # Mueve la comida especial fuera de la pantalla
        self.refresh()  # Llama al método refresh para que la comida normal se mueva a una nueva ubicación

    def reset_after_time_limit(self, time_limit):
        if self.is_special and time.time() - self.special_food_start_time >= time_limit:
            self.reset_special_food()
            self.refresh()