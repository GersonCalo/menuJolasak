import turtle
import time
import random

atzeratu = 0.1

# kontagiluak

puntuak = 0
puntu_Max = 2


# lehioaren konfigurazioa

leihoa = turtle.Screen()
leihoa.title("Sugearen jokoa ")
leihoa.bgcolor("#80ff00")
leihoa.setup(width=600, height=600)
leihoa.tracer(0)

# burua

burua = turtle.Turtle()
burua.speed(0)
burua.shape("square")
burua.penup()
burua.goto(0, 0)
burua.direction = "stop"

# sagarra

sagarra = turtle.Turtle()
sagarra.penup()
sagarra.speed(0)
sagarra.shape("circle")
sagarra.color("red")
sagarra.goto(0, 100)


gorpuak = []


# Puntuazioa
puntuazioa = turtle.Turtle()
puntuazioa.speed(0)
puntuazioa.shape("square")
puntuazioa.color("white")
puntuazioa.penup()
puntuazioa.hideturtle()
puntuazioa.goto(0, 260)
puntuazioa.write("Puntuak: 0  puntuaziorik altuena: 0",align="center", font=("Times", 15, "bold"))


# funciones
def go_up():
    if burua.direction != "down":
        burua.direction = "up"


def go_down():
    if burua.direction != "up":
        burua.direction = "down"


def go_left():
    if burua.direction != "right":
        burua.direction = "left"


def go_rigth():
    if burua.direction != "left":
        burua.direction = "right"


def move():
    if burua.direction == "up":
        burua.sety(burua.ycor()+20)

    if burua.direction == "down":
        burua.sety(burua.ycor()-20)
        
    if burua.direction == "left":
        burua.setx(burua.xcor()-20)

    if burua.direction == "rigth":
        burua.setx(burua.xcor()+20)

    

# teklatu gidatu


leihoa.listen()
leihoa.onkeypress(go_up, "W")
leihoa.onkeypress(go_down, "S")
leihoa.onkeypress(go_left, "A")
leihoa.onkeypress(go_rigth, "D")

# jolasaren buklea
while True:
    leihoa.update()

    if burua.xcor() > 290 or burua.xcor() < -290 or burua.ycor() > 290 or burua.ycor() < -290:
        time.sleep(1)
        burua.goto(0, 0)
        burua.direction = "stop"

        for gorpua in gorpuak:
            gorpua.goto(1000, 1000)

        gorpuak.clear()

        puntuak = 0

        atzeratu = 0.1

        puntuazioa.clear()

        puntuazioa.write("Puntuak:{}  puntuaziorik altuena: {}".format(puntuak, puntu_Max), align="center", font=("Times", 15, "bold"))

    if burua.distance(sagarra) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)

        sagarra.goto( x , y )

        gorpu_berria = turtle.Turtle()
        gorpu_berria.speed(0)
        gorpu_berria.shape("square")
        gorpu_berria.color("grey")
        gorpu_berria.penup()
        gorpuak.append(gorpu_berria)

        atzeratu -= 0.001

        puntuak += 10

        if puntuak > puntu_Max:
            puntu_Max = puntuak

        puntuazioa.clear()
        puntuazioa.write("Puntuak:{}  puntuaziorik altuena: {}".format(puntuak, puntu_Max), align="center", font=("Times", 15, "bold"))

    for index in range(len(gorpuak)-1, 0, -1):
        x = gorpuak[index-1].xcor()
        y = gorpuak[index-1].ycor()
        gorpuak[index].goto(x, y)

    if len(gorpuak) > 0:
        x = burua.xcor()
        y = burua.ycor()
        gorpuak[0].goto(x, y)

    move()

    for gorpua in gorpuak:
        if gorpua.distance(burua) < 20:
            time.sleep(1)
            burua.goto(0, 0)
            burua.direction = "stop"

            for gorpua in gorpuak:
                gorpua.goto(1000, 1000)

            gorpuak.clear()

            puntuak = 0

            atzeratu = 0.1

            puntuazioa.clear()
            puntuazioa.write("Puntuak:{}  puntuaziorik altuena: {}".format(puntuak, puntu_Max), align="center", font=("Times", 15, "bold"))
    time.sleep(atzeratu)

leihoa.mainloop()
