# EXERCÍCIO: Desenhar um cenário com a biblioteca turtle.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import turtle

t = turtle.Turtle()

# colocando a tartaruga na borda inferior 
t.up()
t.goto(-400,-300)
t.down()

# fazendo a grama
t.color('green')
t.fillcolor('green')
t.begin_fill()
t.fd(800)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(800)
t.lt(90)
t.fd(100)
t.end_fill()

# voltando pro mesmo ponto
t.lt(180)
t.fd(100)
t.rt(90)

# fazendo o céu
t.color('lightblue')
t.fillcolor('lightblue')
t.begin_fill()
t.fd(800)
t.lt(90)
t.fd(500)
t.lt(90)
t.fd(800)
t.lt(90)
t.fd(500)
t.lt(90)
t.end_fill()

# posicionando para a casa
t.fd(200)
t.lt(90)

# parede casa
t.color('gray')
t.fillcolor('gray')
t.begin_fill()
t.fd(180)
t.rt(90)
t.fd(180)
t.rt(90)
t.fd(180)
t.rt(90)
t.fd(180)
t.rt(90)
t.end_fill()

# posicinando para a porta
t.rt(90)
t.fd(110)
t.lt(90)

# porta casa
t.color('brown')
t.fillcolor('brown')
t.begin_fill()
t.fd(110)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(110)
t.rt(90)
t.fd(50)
t.rt(90)
t.end_fill()

# posicionando maçaneta
t.fd(50)
t.rt(90)
t.fd(10)

# maçaneta casa
t.color('black')
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()

# posicionando janela
t.up()
t.goto(-180, -160)
t.down()

# janela casa
t.color('white')
t.fillcolor('black')
t.begin_fill()
t.fd(70)
t.lt(90)
t.fd(70)
t.lt(90)
t.fd(70)
t.lt(90)
t.fd(70)
t.lt(90)
t.end_fill()
t.fd(35)
t.lt(90)
t.fd(70)
t.lt(90)
t.fd(35)
t.lt(90)
t.fd(35)
t.lt(90)
t.fd(70)
t.lt(90)

# posicionando telhado
t.up()
t.goto(-200,-20)
t.down()

# telhado casa
t.color('orange')
t.fillcolor('orange')
t.begin_fill()
t.rt(90)
t.fd(180)
t.lt(120)
t.fd(180)
t.lt(120)
t.fd(180)
t.end_fill()

# posicionando a arvore
t.up()
t.goto(200,-200)
t.down()
t.rt(150)

# tronco arvore
t.color('brown')
t.fillcolor('brown')
t.begin_fill()
t.fd(120)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(120)
t.rt(90)
t.fd(30)
t.rt(90)
t.end_fill()

# copa
t.fd(100)
t.rt(90)
t.fd(15)

t.color('green')
t.fillcolor('green')
t.begin_fill()
t.circle(70)
t.rt(90)
t.end_fill()

# posicionando sol
t.up()
t.goto(-250, 150)
t.lt(180)
t.down()


# o sol
t.color('yellow')
t.fillcolor('yellow')
t.begin_fill()
t.circle(45)
t.end_fill()
t.lt(90)
t.fd(45)

# raios
t.width(5)
t.fd(75)
t.bk(75)
t.lt(60)
t.fd(75)
t.bk(75)
t.lt(60)
t.fd(75)
t.bk(75)
t.lt(60)
t.fd(75)
t.bk(75)
t.lt(60)
t.fd(75)
t.bk(75)
t.lt(60)
t.fd(75)
t.bk(75)
t.width()

# posicionando nuvem
t.rt(30)
t.up()
t.goto(0, 200)
t.down()

# nuvem
t.color('white')
t.fillcolor('white')
t.begin_fill()
t.circle(-40)
t.end_fill()

t.rt(90)
t.fd(40)

t.color('white')
t.fillcolor('white')
t.begin_fill()
t.circle(-40)
t.end_fill()

t.rt(90)
t.fd(40)

t.color('white')
t.fillcolor('white')
t.begin_fill()
t.circle(-40)
t.end_fill()

t.lt(90)
t.fd(100)

t.color('white')
t.fillcolor('white')
t.begin_fill()
t.circle(-40)
t.end_fill()

t.rt(90)
t.fd(40)

t.color('white')
t.fillcolor('white')
t.begin_fill()
t.circle(-40)
t.end_fill()

t.rt(90)
t.fd(40)

t.color('white')
t.fillcolor('white')
t.begin_fill()
t.circle(-40)
t.end_fill()

