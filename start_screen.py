import turtle
import subprocess

file_name = 'snake_game.py'

o_simulakra = turtle.Screen()
o_simulakra.title("SNAKE")
o_simulakra.setup(width=1500, height=750)
o_simulakra.bgcolor("blue")
# o_simulakra.tracer(0)
# tracer() fonksiyonu çalıştığı taktirde selector otomatik biçimde gizleniyor.

opening = turtle.Turtle()
opening.speed(0)
opening.color('black')
opening.shape('square')
opening.penup()
opening.goto(0, 40)
opening.hideturtle()
opening.write('YILAN OYUNU', align='center', font=('Arial', 50, 'bold'))

start_button = turtle.Turtle()
start_button.speed(0)
start_button.color('black')
start_button.shape('square')
start_button.penup()
start_button.goto(0, -10)
start_button.hideturtle()
start_button.write('BAŞLA', align='center', font=('Arial', 25, 'normal'))

exit_button = turtle.Turtle()
exit_button.speed(0)
exit_button.color('black')
exit_button.shape('square')
exit_button.penup()
exit_button.goto(0, -60)
exit_button.hideturtle()
exit_button.write('ÇIKIŞ', align='center', font=('Arial', 25, 'normal'))

selector = turtle.Turtle()
selector.speed(0)
selector.color('yellow')
selector.shape('triangle')
selector.penup()
selector.goto(-80, 10)

# Seçim durumunu kontrol et
selected = 'start'


# Yön tuşlarına basıldığında ne olacağını tanımla
def go_up():
    global selected
    if selected == 'exit':
        selector.goto(-80, 10)
        selected = 'start'


def go_down():
    global selected
    if selected == 'start':
        selector.goto(-80, -40)
        selected = 'exit'


def select():
    if selected == 'start':
        print("Start'a tıklandı!")
        o_simulakra.bye()
        subprocess.run(['python', file_name])
    elif selected == 'exit':
        print("Exit'e tıklandı!")
        exit()


# Tuş vuruşlarını ekranla ilişkilendir
o_simulakra.listen()
o_simulakra.onkey(go_up, 'Up')
o_simulakra.onkey(go_down, 'Down')
o_simulakra.onkey(select, 'Return')


# Tıklama olaylarını tanımla
def on_click(x, y):
    if start_button.distance(x, y) < 50:
        print("Start'a tıklandı!")
        o_simulakra.bye()
        subprocess.run(['python', file_name])
    elif exit_button.distance(x, y) < 50:
        print("Exit'e tıklandı!")
        exit()


# Tıklama olayını ekranla ilişkilendir
o_simulakra.onscreenclick(on_click)

# Olay döngüsünü başlat
turtle.done()
