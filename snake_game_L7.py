"""snake game - level 7"""
#  TODO
#   1. b_sol exit()
#   2. b_ust exit()
#   3. b_sag exit()
#   4. b_orta exit()
#   5. b_alt exit()
#   6. e_sol exit()
#   7. e_ust exit()
#   8. e_orta exit()
#   9. e_alt exit()
#   10. m_sol exit()
#   11. m_sag exit()
#   12. m_ust exit()
#   13. m_orta exit()

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
    head.goto(150, 150)
    head.direction = 'stop'
    head_speed = 0.05

    """B HARFİ"""
    b_sol = turtle.Turtle()
    b_sol.width(30)
    b_sol.penup()
    b_sol.goto(-350, -250)
    b_sol.pendown()
    b_sol.setheading(90)
    b_sol.forward(500)

    b_ust = turtle.Turtle()
    b_ust.width(30)
    b_ust.penup()
    b_ust.goto(-350, 250)
    b_ust.pendown()
    b_ust.forward(200)

    b_sag = turtle.Turtle()
    b_sag.width(30)
    b_sag.penup()
    b_sag.goto(-150, -250)
    b_sag.pendown()
    b_sag.setheading(90)
    b_sag.forward(500)

    b_orta = turtle.Turtle()
    b_orta.width(30)
    b_orta.penup()
    b_orta.goto(-275, 50)
    b_orta.pendown()
    b_orta.forward(125)

    b_alt = turtle.Turtle()
    b_alt.width(30)
    b_alt.penup()
    b_alt.goto(-275, -250)
    b_alt.pendown()
    b_alt.forward(125)

    """E HARFİ"""
    e_sol = turtle.Turtle()
    e_sol.width(30)
    e_sol.penup()
    e_sol.goto(-50, -250)
    e_sol.pendown()
    e_sol.setheading(90)
    e_sol.forward(500)

    e_ust = turtle.Turtle()
    e_ust.width(30)
    e_ust.penup()
    e_ust.goto(-50, 250)
    e_ust.pendown()
    e_ust.forward(150)

    e_orta = turtle.Turtle()
    e_orta.width(30)
    e_orta.penup()
    e_orta.goto(-50, 50)
    e_orta.pendown()
    e_orta.forward(125)

    e_alt = turtle.Turtle()
    e_alt.width(30)
    e_alt.penup()
    e_alt.goto(-50, -250)
    e_alt.pendown()
    e_alt.forward(150)

    """M HARFİ"""
    m_sol = turtle.Turtle()
    m_sol.width(30)
    m_sol.penup()
    m_sol.goto(200, -250)
    m_sol.pendown()
    m_sol.setheading(90)
    m_sol.forward(500)

    m_sag = turtle.Turtle()
    m_sag.width(30)
    m_sag.penup()
    m_sag.goto(450, -250)
    m_sag.pendown()
    m_sag.setheading(90)
    m_sag.forward(500)

    m_ust = turtle.Turtle()
    m_ust.width(30)
    m_ust.penup()
    m_ust.goto(200, 250)
    m_ust.pendown()
    m_ust.forward(250)

    m_orta = turtle.Turtle()
    m_orta.width(30)
    m_orta.penup()
    m_orta.goto(325, 100)
    m_orta.pendown()
    m_orta.setheading(90)
    m_orta.forward(150)

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
        if head.xcor() > 750:
            head.goto(-750, head.ycor())

        if head.xcor() < -750:
            head.goto(750, head.ycor())

        if head.ycor() > 375:
            head.goto(head.xcor(), -375)

        if head.ycor() < -375:
            head.goto(head.xcor(), 375)

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

        for b_sol_ in range(-250, 260, 10):
            if head.distance(-350, b_sol_) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(-350, b_sol_) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for b_ust_ in range(-350, -160, 10):
            if head.distance(b_ust_, 250) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(b_ust_, 250) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for b_sag_ in range(-250, 260, 10):
            if head.distance(-150, b_sag_) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(-150, b_sag_) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for b_orta_ in range(-275, -155, 5):
            if head.distance(b_orta_, 50) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(b_orta_, 50) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for b_alt_ in range(-275, -155, 5):
            if head.distance(b_alt_, -250) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(b_alt_, -250) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for e_sol_ in range(-250, 260, 10):
            if head.distance(-50, e_sol_) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(-50, e_sol_) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for e_ust_ in range(-50, 110, 10):
            if head.distance(e_ust_, 250) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(e_ust_, 250) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for e_orta_ in range(-50, 80, 5):
            if head.distance(e_orta_, 50) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(e_orta_, 50) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for e_alt_ in range(-50, -160, 5):
            if head.distance(e_alt_, -250) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(e_alt_, -250) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for m_sol_ in range(-250, 260, 10):
            if head.distance(200, m_sol_) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(200, m_sol_) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for m_sag_ in range(-250, 260, 10):
            if head.distance(450, m_sag_) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(450, m_sag_) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for m_ust_ in range(200, 460, 10):
            if head.distance(m_ust_, 250) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(m_ust_, 250) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        for m_orta_ in range(100, 260, 10):
            if head.distance(325, m_orta_) < 20:
                time.sleep(1)
                print("YOUR SCORE: ", score)
                print("GOODBYE")
                exit()
            if prey.distance(325, m_orta_) < 20:
                x = random.randint(-350, 350)
                y = random.randint(-350, 350)
                prey.goto(x, y)

        move()
        time.sleep(head_speed)
