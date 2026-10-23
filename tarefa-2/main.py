# EXERCÍCIO: Desenhar formas geométricas com a biblioteca turtle.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import turtle
t = turtle.Turtle()

def figura(n, tam):
    t.down()
    for i in range(n):
        t.fd(tam)
        t.rt(360/n)
    t.up()

t.bk(400)
t.fd(800)
t.stamp()
t.up()
t.goto(0, -300)
t.lt(90)
t.down()
t.fd(600)
t.stamp()
t.up()

t.goto(50, 50)
figura(4, 200)

t.goto(-300, 100)
figura(6, 100)

t.goto(-300, -200)
figura(9, 80)

t.goto(80, -300)
figura(4, 240)
t.goto(95, -285)
figura(4, 210)
t.goto(110, -270)
figura(4, 180)
t.goto(125, -255)
figura(4, 150)
t.goto(140, -240)
figura(4, 120)
t.goto(155, -225)
figura(4, 90)
t.goto(170, -210)
figura(4, 60)
t.goto(185, -195)
figura(4, 30)

