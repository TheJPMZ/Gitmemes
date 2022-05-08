import turtle

def init():
    turtle.setup(width=600, height=600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    
def draw_head():
    turtle.right(90)
    turtle.circle(25)
    turtle.penup()
    turtle.left(90)
    turtle.forward(150)
    turtle.pendown()


def draw_body():
    turtle.forward(-100)


def draw_rifht_arm():
    turtle.right(45)
    turtle.forward(100)
    turtle.forward(-100)
    turtle.left(45)


def draw_left_arm():
    turtle.left(45)
    turtle.forward(100)
    turtle.forward(-100)
    turtle.right(45)

def draw_right_leg():
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.forward(-100)
    turtle.left(45)

def draw_sentence(text):
    origin = turtle.position()
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.write(text.lower(), font=("Courier", 40, "bold"))
    turtle.goto(origin)
    turtle.pendown()