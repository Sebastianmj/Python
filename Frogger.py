#-- coding: utf-8 --
import turtle
import time 
import random



def main ():

    configscreen() #Llamado a función principal

#Configuración de la pantalla
def configscreen():
    global screen 
    screen = turtle.Screen() 
    screen.title("Parcial Frogger") #Título de la ventana
    screen.bgcolor("black") #Color de la ventana
    screen.setup(1000,600) #Tamaño de la ventana
    controles() #Llamado a controles de Frogger(Jugador)
    Tronco1() #Llamado a objeto Tronco
    Tronco2() #Llamado a objeto Tronco
    Tronco3() #Llamado a objeto Tronco
    Carro1() #Llamado a objeto carro
    Carro2() #Llamado a objeto carro
    Carro3() #Llamado a objeto carro
    JugadorFrogger() #Llamado a Frogger
    
#Título
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("white")
    texto.penup()
    texto.hideturtle()
    texto.goto(0,260)
    texto.write("Juego Frogger", align= "center", font =("Courier", 24, "normal"))

    while True:
        screen.update() 

#Ganó
        if Frogger.ycor() > 260:
            texto.goto(0,0)
            texto.write("Ganaste", align= "center", font =("Courier", 24, "normal"))
            Frogger.goto(0,-100)

#Colisiones
        if Frogger.distance(tronco_1) < 40:
            Frogger.goto(0,-250)
            Frogger.direction = "stop"
            texto.goto(0,0)
            texto.write("Perdiste", align= "center", font =("Courier", 24, "normal"))        
        if Frogger.distance(tronco_2) < 40:
            Frogger.goto(0,-250)
            Frogger.direction = "stop"
            texto.goto(0,0)
            texto.write("Perdiste", align= "center", font =("Courier", 24, "normal"))
        if Frogger.distance(tronco_3) < 40:
            Frogger.goto(0,-250)
            Frogger.direction = "stop"
            texto.goto(0,0)
            texto.write("Perdiste", align= "center", font =("Courier", 24, "normal"))
        if Frogger.distance(carro1) < 40:
            Frogger.goto(0,-250)
            Frogger.direction = "stop"
            texto.goto(0,0)
            texto.write("Perdiste", align= "center", font =("Courier", 24, "normal"))
        if Frogger.distance(carro2) < 40:
            Frogger.goto(0,-250)
            Frogger.direction = "stop"
            texto.goto(0,0)
            texto.write("Perdiste", align= "center", font =("Courier", 24, "normal"))        
        if Frogger.distance(carro3) < 40:
            Frogger.goto(0,-250)
            Frogger.direction = "stop"
            texto.goto(0,0)
            texto.write("Perdiste", align= "center", font =("Courier", 24, "normal"))

#Movimiento de obstaculos            
        movTronco()
        movTronco_2()
        movTronco_3()
        movCarro1()
        movCarro2()      
        movCarro3()      
#Creación de jugador Frogger
def JugadorFrogger():
    global Frogger #Se genera variable para usar fuera de la función
    Frogger = turtle.Turtle() #Crea el objeto Frogger
    Frogger.shape("turtle")#Define forma de Frogger
    Frogger.color("green")#define el color de Frogger
    Frogger.penup()#Borra el rastreo del movimiento
    Frogger.goto(0,-250)#Define la posición de Frogger
    Frogger.direction = "stop"

def MoverFrogger_Up():
    y = Frogger.ycor()
    y += 20
    Frogger.sety(y) #Define el valor de Frogger en el eje Y
    print(y)

def MoverFrogger_Down():
    y = Frogger.ycor()
    y -= 20
    Frogger.sety(y) #Define el valor de Frogger en el eje Y
    print(y)

def MoverFrogger_Right():
    x = Frogger.xcor()
    x += 20
    Frogger.setx(x) #Define el valor de Frogger en el eje X
    print(x)

def MoverFrogger_Left():
    x = Frogger.xcor()
    x -= 20
    Frogger.setx(x) #Define el valor de Frogger en el eje X
    print(x)

def controles():
    screen.listen()
    screen.onkeypress(MoverFrogger_Up, "Up") #Movimiento con la tecla ↑
    screen.onkeypress(MoverFrogger_Down, "Down") #Movimiento con la tecla ↓
    screen.onkeypress(MoverFrogger_Right, "Right") #Movimiento con la tecla →
    screen.onkeypress(MoverFrogger_Left, "Left") #Movimiento con la tecla ←

#Creación de Tronco 1
def Tronco1():
    global tronco_1
    tronco_1 = turtle.Turtle()
    tronco_1.speed(0)
    tronco_1.shape("square")
    tronco_1.color("red")
    tronco_1.penup()
    tronco_1.shapesize(1,4)

#Función movimiento
def movTronco():
    tronco_1.dx = -25 
    tronco_1.setx(tronco_1.xcor() + tronco_1.dx)
    if tronco_1.xcor() > 290:
        tronco_1.goto(0,-290)
        tronco_1.dx *= -1
    if tronco_1.xcor() < -290:
        tronco_1.goto(290,200)
        tronco_1.dx *= -1

#Creación de Tronco 2
def Tronco2():
    global tronco_2
    tronco_2 = turtle.Turtle()
    tronco_2.speed(0)
    tronco_2.shape("square")
    tronco_2.color("red")
    tronco_2.penup()
    tronco_2.shapesize(1,4)

#Función movimiento
def movTronco_2():
    tronco_2.dx = -35 
    tronco_2.setx(tronco_2.xcor() + tronco_2.dx)
    if tronco_2.xcor() > 290:
        tronco_2.goto(0,-290)
        tronco_2.dx *= -1
    if tronco_2.xcor() < -290:
        tronco_2.goto(290,150)
        tronco_2.dx *= -1

#Creación de Tronco 3
def Tronco3():
    global tronco_3
    tronco_3 = turtle.Turtle()
    tronco_3.speed(0)
    tronco_3.shape("square")
    tronco_3.color("red")
    tronco_3.penup()
    tronco_3.shapesize(1,4)

#Función movimiento
def movTronco_3():
    tronco_3.dx = -40 
    tronco_3.setx(tronco_3.xcor() + tronco_3.dx)
    if tronco_3.xcor() > 290:
        tronco_3.goto(0,-290)
        tronco_3.dx *= -1
    if tronco_3.xcor() < -290:
        tronco_3.goto(290,100)
        tronco_3.dx *= -1

#Creación de carro 1
def Carro1():
    global carro1
    carro1 = turtle.Turtle()
    carro1.speed(0)
    carro1.shape("square")
    carro1.color("blue")
    carro1.penup()
    carro1.shapesize(1,1)

#Función movimiento
def movCarro1():
    carro1.dx = -30 
    carro1.setx(carro1.xcor() + carro1.dx)
    if carro1.xcor() > 290:
        carro1.goto(0,-290)
        carro1.dx *= -1
    if carro1.xcor() < -290:
        carro1.goto(290,50)
        carro1.dx *= -1

#Creación de carro 2
def Carro2():
    global carro2
    carro2 = turtle.Turtle()
    carro2.speed(0)
    carro2.shape("square")
    carro2.color("blue")
    carro2.penup()
    carro2.shapesize(1,1)

#Función movimiento
def movCarro2():
    carro2.dx = -20 
    carro2.setx(carro2.xcor() + carro2.dx)
    if carro2.xcor() > 290:
        carro2.goto(0,-290)
        carro2.dx *= -1
    if carro2.xcor() < -290:
        carro2.goto(290,0)
        carro2.dx *= -1


#Creación de carro 3
def Carro3():
    global carro3
    carro3 = turtle.Turtle()
    carro3.speed(0)
    carro3.shape("square")
    carro3.color("white")
    carro3.penup()
    carro3.shapesize(1,2)

#Función movimiento
def movCarro3():
    carro3.dx = -10 
    carro3.setx(carro3.xcor() + carro3.dx)
    if carro3.xcor() > 290:
        carro3.goto(0,-290)
        carro3.dx *= -1
    if carro3.xcor() < -290:
        carro3.goto(290,0)
        carro3.dx *= -1


if __name__ == "__main__":
    main()

