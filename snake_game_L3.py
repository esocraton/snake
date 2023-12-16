"""snake game - level 3"""

import turtle
import time
import random


kezban = False
while True:
    simulakra = turtle.Screen()
    simulakra.title("SNAKE")
    simulakra.setup(width=1500, height=750)
    simulakra.bgcolor("blue")
    simulakra.tracer(0)

    head = turtle.Turtle()
    head.speed(0)
    head.color("yellow")
    head.shape("circle")
    head.penup()
    head.goto(0, 0)
    head.direction = 'stop'
    head_speed = 0.05

    flat_wall = turtle.Turtle()
    flat_wall.width(30)
    flat_wall.penup()
    flat_wall.goto(-400, 125)
    flat_wall.pendown()
    flat_wall.forward(800)

    flat_wall_2 = turtle.Turtle()
    flat_wall_2.width(30)
    flat_wall_2.penup()
    flat_wall_2.goto(-400, -125)
    flat_wall_2.pendown()
    flat_wall_2.forward(800)

    prey = turtle.Turtle()
    prey.speed(0)
    prey.color('white')
    prey.shape('square')
    prey.penup()
    prey.goto(-300, 0)
    prey.shapesize(0.5, 0.5)

    body = []
    score = 0

    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.color('yellow')
    score_board.shape('square')
    score_board.penup()
    score_board.goto(0, 300)
    score_board.hideturtle()
    score_board.write('SCORE: {}'.format(score), align='center', font=('Courier', 25, 'normal'))


    def move():
        """oyuncunun hareketlerini ayarlıyoruz"""
        if head.direction == 'up':
            y = head.ycor()
            head.sety(y + 10)
        if head.direction == 'down':
            y = head.ycor()
            head.sety(y - 10)
        if head.direction == 'left':
            x = head.xcor()
            head.setx(x - 10)
        if head.direction == 'right':
            x = head.xcor()
            head.setx(x + 10)


    def move_up():
        """oyuncu yukarı giderken birden aşağı gidemesin"""
        if head.direction != 'down':
            head.direction = 'up'


    def move_down():
        """oyuncu aşağı giderken birden yukarı gidemesin"""
        if head.direction != 'up':
            head.direction = 'down'


    def move_left():
        """oyuncu sola giderken birden sağa gidemesin"""
        if head.direction != 'right':
            head.direction = 'left'


    def move_right():
        """oyuncu sağa giderken birden sola gidemesin"""
        if head.direction != 'left':
            head.direction = 'right'


    simulakra.listen()
    simulakra.onkey(move_up, 'Up')
    simulakra.onkey(move_down, 'Down')
    simulakra.onkey(move_right, 'Right')
    simulakra.onkey(move_left, 'Left')

    while True:
        simulakra.update()
        if head.xcor() > 750 or head.xcor() < -750 or head.ycor() > 375 or head.ycor() < -375:
            time.sleep(1)
            print("YOUR SCORE: ", score)
            print("GOODBYE")
            time.sleep(3)
            kezban = True
            break

        if head.distance(prey) < 20:
            if score < 100:
                x = random.randint(-75, 75)
                y = random.randint(-75, 75)
                prey.goto(x, y)
            if 100 < score < 250:
                x = random.randint(-100, 100)
                y = random.randint(-100, 100)
                prey.goto(x, y)
            if 250 < score < 500:
                x = random.randint(-150, 150)
                y = random.randint(-150, 150)
                prey.goto(x, y)
            if 500 < score < 750:
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                prey.goto(x, y)
            if score > 750:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

            score += 10
            score_board.clear()
            score_board.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))
            head_speed = head_speed - 0.0003

            tail = turtle.Turtle()
            tail.speed(0)
            tail.color('yellow')
            tail.shape('circle')
            tail.penup()
            body.append(tail)

        if len(body) > 0:
            x = head.xcor()
            y = head.ycor()
            body[0].goto(x, y)

        for i in range(len(body) - 1, 0, -1):
            x = body[i - 1].xcor()
            y = body[i - 1].ycor()
            body[i].goto(x, y)

        if len(body) > 3:
            anan = body[2:]
            for an in anan:
                if prey.distance(an) < 20:
                    x = random.randint(-350, 350)
                    y = random.randint(-350, 350)
                    prey.goto(x, y)
                if head.distance(an) < 1:
                    time.sleep(1)
                    simulakra.clear()
                    simulakra.bgcolor("blue")
                    simulakra.tracer(0)
                    time.sleep(1)
                    print("YOUR SCORE: ", score)
                    print("GOODBYE")
                    exit()

        x_distance = -400
        for x_distance in range(-400, 410, 10):
            if head.distance(x_distance, 125) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(x_distance, 125) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        x_distance_2 = -400
        for x_distance_2 in range(-400, 410, 10):
            if head.distance(x_distance_2, -125) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(x_distance_2, 125) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        move()
        time.sleep(head_speed)

    if kezban:
        break
