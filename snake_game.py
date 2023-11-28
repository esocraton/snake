import turtle
import time
import random

"""ekranı ayarlıyoruz"""
simulakra = turtle.Screen()
# burada oyun için platform oluşturuyoruz
simulakra.title("SNAKE")
# burada platforma başlık koyuyoruz
simulakra.setup(width=1500, height=750)
# burada platformun boyutlarını ayarlıyoruz
simulakra.bgcolor("blue")
# burada platformun arkaplan rengini ayarlıyoruz
simulakra.tracer(0)
# burada platformun kendini tekrar etmesini engelliyoruz

"""yılanın başını ayarlıyoruz"""
head = turtle.Turtle()
# yılanın başını oluşturduk
head.speed(0)
# yılan başının hareket hızını belirledik
head.color("yellow")
# yılan başının rengini belirledik
head.shape("circle")
# yılan başının şeklini belirledik
head.penup()
# yılan başı hareket ederken arkasından şekil çıkmasını durdurduk
head.goto(0, 0)
# yılan başının yerleşeceği koordinatı yazdık
head.direction = 'stop'
# yılan başının yapacağı hareketi belirledik

"""yem ayarlıyoruz"""
prey = turtle.Turtle()
prey.speed(0)
prey.color('white')
prey.shape('square')
prey.penup()
prey.goto(-300, 0)
prey.shapesize(0.5, 0.5)


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
    # bu while döngüsüyle oyunun direkt kapanmasını engelliyoruz
    move()
    # oyuncunun hareket etmesini sağlıyoruz
    time.sleep(0.05)
    # head'ın hızını düşürüp ateşini alıyoruz
    if head.distance(prey) < 10:
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        prey.goto(x, y)
