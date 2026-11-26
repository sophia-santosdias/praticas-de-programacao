# EXERCÍCIO: Elaborar um programa para simular uma corrida de tartarugas, onde cada tartaruga avança uma distância aleatória a cada jogada. O programa deve terminar indicando qual tartaruga chegou primeiro à linha de chegada.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import turtle
import random

#fazer a pista
t0 = turtle.Turtle()
t0.ht()
t0.up()
t0.goto(-400, 200)
t0.down()
t0.fd(800)

t0.up()
t0.goto(-400, 0)
t0.down()
t0.fd(800)

t0.up()
t0.goto(-400, -200)
t0.down()
t0.fd(800)

t0.up()
t0.goto(400, 250)
t0.width(7)
t0.down()
t0.goto(400, -250)

#criar tartarugas
t1 = turtle.Turtle(shape='turtle')
t2 = turtle.Turtle(shape='turtle')
t3 = turtle.Turtle(shape='turtle')

t1.color('blue')
t1.up()
t1.goto(-400, 200)

t2.color('red')
t2.up()
t2.goto(-400, 0)

t3.color('gold')
t3.up()
t3.goto(-400, -200)

tart = [t1, t2, t3]

#loop de jogadas
while t1.xcor() < 400 and t2.xcor() < 400 and t3.xcor() < 400:
    for t in tart:
        dado = random.randint(1, 6)
        x = 25 * dado
        t.goto(t.xcor()+ x, t.ycor())
        if t.xcor() >= 400:
            break

t0.up()
t0.goto(0, 300)
if t1.xcor() >= 400:
    t0.write("Tartaruga azul venceu", align='center', font=('Arial', 14, 'normal'))

if t2.xcor() >= 400:
    t0.write("Tartaruga vermelha venceu", align='center',font=('Arial', 14, 'normal'))

if t3.xcor() >= 400:
    t0.write("Tartaruga amarela venceu", align='center',font=('Arial', 14, 'normal'))







        
        
