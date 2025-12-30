import turtle 

# Configuramos la pamtalla del juego
window = turtle.Screen()
window.title("Juego de Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) 

# Marcador
puntuacion_a = 0
puntuacion_b = 0

# Bloque A
bloque_a = turtle.Turtle()
bloque_a.speed(0) #velocidad máxima
bloque_a.shape("square")
bloque_a.color("white")
bloque_a.shapesize(stretch_wid=5, stretch_len=1)
bloque_a.penup()
bloque_a.goto(-350, 0)

# Bloque B
bloque_b = turtle.Turtle()
bloque_b.speed(0) #velocidad máxima
bloque_b.shape("square")
bloque_b.color("white")
bloque_b.shapesize(stretch_wid=5, stretch_len=1)
bloque_b.penup()
bloque_b.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.2
pelota.dy = -0.2

# Puntuación
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Jugador A: {puntuacion_a}  Jugador B: {puntuacion_b}", align="center", font=("Courier", 24, "normal"))

# Mover los bloques
def bloque_a_up():
    y = bloque_a.ycor()
    y += 20
    bloque_a.sety(y)

def bloque_a_down():
    y = bloque_a.ycor()
    y -= 20
    bloque_a.sety(y)

def bloque_b_up():
    y = bloque_b.ycor()
    y += 20
    bloque_b.sety(y)

def bloque_b_down():
    y = bloque_b.ycor()
    y -= 20
    bloque_b.sety(y)

# Designar las teclas que el sistema debe atender
window.listen()
window.onkeypress(bloque_a_up, "w")
window.onkeypress(bloque_a_down, "s")
window.onkeypress(bloque_b_up, "Up")
window.onkeypress(bloque_b_down, "Down")

# Bucle principal con el que comprobamos las colisiones y salidas de la pantalla
while True:
    window.update()

    # para mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # colisiones con los bordes
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1 #invierte direccion de la pelota

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # si la pelota sale de la pantalla por los lados
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntuacion_a += 1
        pen.clear()
        pen.write(f"Jugador A: {puntuacion_a}  Jugador B: {puntuacion_b}", align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntuacion_b += 1
        pen.clear()
        pen.write(f"Jugador A: {puntuacion_a}  Jugador B: {puntuacion_b}", align="center", font=("Courier", 24, "normal"))

    # Colisiones con los bloques
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < bloque_b.ycor() + 50 and pelota.ycor() > bloque_b.ycor() - 50):
        pelota.setx(340)
        pelota.dx *= -1

    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < bloque_a.ycor() + 50 and pelota.ycor() > bloque_a.ycor() - 50):
        pelota.setx(-340)
        pelota.dx *= -1