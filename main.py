import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
all_cars = []
game_is_on = True
moves = 5
player = Player()
level = 0
while game_is_on:
    time.sleep(0.1)


    # Спавн машины раз в 5 проходок
    if moves == 5:
        car = CarManager(random.randint(-260, 260),level)
        all_cars.append(car)
        moves = 0
    else:
        moves += 1


        # Движение всех машин
    for car in all_cars:
        car.move()
        if player.distance(car) < 25:
            game_is_on = False
        if player.ycor() > 280:
            level += 1
            for car in all_cars:
                all_cars.remove(car)
                car.hideturtle()
            player.respawn()

    # ходьба для черепахи
    screen.listen()
    screen.onkeypress(player.move_forward,'w')
    screen.update()






screen.exitonclick()
