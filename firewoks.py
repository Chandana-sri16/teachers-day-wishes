import turtle
import random
import time
import winsound


wn = turtle.Screen()
wn.setup()
wn.bgcolor('black')

winsound.PlaySound('countdown.wav', winsound.SND_ASYNC)

myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.color('white')
myTurtle.goto(0, -100)
myTurtle.write("3", align='center', font=("Cooper Black", 200, 'bold'))
myTurtle.hideturtle()
time.sleep(1)
myTurtle.clear()

myTurtle.penup()
myTurtle.color('white')
myTurtle.goto(0, -100)
myTurtle.write("2", align='center', font=("Cooper Black", 200, 'bold'))
myTurtle.hideturtle()
time.sleep(1)
myTurtle.clear()

myTurtle.penup()
myTurtle.color('white')
myTurtle.goto(0, -100)
myTurtle.write("1", align='center', font=("Cooper Black", 200, 'bold'))
myTurtle.hideturtle()
time.sleep(1)
myTurtle.clear()

myTurtle.penup()
myTurtle.color('white')
myTurtle.goto(0, -100)
myTurtle.write("Go", align='center', font=("Cooper Black", 150, 'bold'))
myTurtle.hideturtle()
time.sleep(1)
myTurtle.clear()

winsound.PlaySound('Diwali ! Rocket Crackers ! Sound.wav', winsound.SND_ASYNC)
myTurtle.speed(-1)
myTurtle.penup()
myTurtle.color('white')
myTurtle.goto(0, -300)
myTurtle.write("""
\n      HAPPY \n  TEACHER'S \n       DAY !
""", align='center', font=("Cooper Black", 100, 'bold'))
myTurtle.hideturtle()

colors = ['red', 'green', 'yellow', 'gold', 'pink', 'cyan', 'white', 'orange',
          'violet', 'coral', 'blue', 'purple', 'magenta', 'silver', 'lime']


def draw_fw(t):
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(colors))
    d = random.randint(20, 100)

    for i in range(36):
        t.forward(d)
        t.backward(d)
        t.right(10)


for i in range(20):
    draw_fw(myTurtle)

myTurtle.penup()
myTurtle.goto(0, 200)


turtle.exitonclick()

