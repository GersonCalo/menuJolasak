import turtle 
import time 

atzeratu = 0.1

#kontagiluak

puntuak=0
puntu_Max=2


#lehioaren konfigurazioa

leihoa=turtle.Screen()
leihoa.title("Sugearen jokoa ")
leihoa.bgcolor("#80ff00")
leihoa.setup(width=600,height=600)
leihoa.tracer(0)

#burua 

burua=turtle.Turtle()
burua.speed(0)
burua.shape("square")
burua.penup()
burua.goto(0,0)
burua.direction="up"

#sagarra

sagarra=turtle.Turtle()
sagarra.speed(0)
sagarra.shape("circle")
sagarra.color("red")
sagarra.goto(0,100)
sagarra.penup()


#Puntuazioa
puntuazioa = turtle.Turtle()
puntuazioa.speed(0)
puntuazioa.shape("square")
puntuazioa.color("white")
puntuazioa.penup()
puntuazioa.hideturtle()
puntuazioa.goto(0, 260)
puntuazioa.write("Puntuak: 0  puntuaziorik altuena: 0", align="center", font=("Times", 15, "bold"))


#funciones
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
        y = burua.ycor
        burua.sety(y+20)

    if burua.direction == "down":
        y = burua.ycor
        burua.sety(y-20)

    if burua.direction == "rigth":
        x = burua.xcor
        burua.setx(x+20)

    if burua.direction == "left":
        x = burua.xcor
        burua.setx(x-20)

#teklatu gidatu

leihoa.listen()
leihoa.onkeypress(go_up, "w")
leihoa.onkeypress(go_down, "s")
leihoa.onkeypress(go_left,"a")
leihoa.onkeypress(go_rigth,"d")

#jolasaren buklea
while True:
    
    leihoa.update()
    
    
    time.sleep(atzeratu)


