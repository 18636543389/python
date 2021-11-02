import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            koch(size/3, n-1)
def main():
    turtle.setup(800, 600)
    turtle.penup()
    turtle.goto(-220, 120)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("red")
    koch(300, 3)
    turtle.right(360/7)
    turtle.pencolor("yellow")
    koch(300, 3)
    turtle.right(360/7)
    turtle.pencolor("blue")
    koch(300, 3)
    turtle.right(360 / 7)
    turtle.pencolor("Orange")
    koch(300, 3)
    turtle.right(360 / 7)
    turtle.pencolor("Green")
    koch(300, 3)
    turtle.right(360 / 7)
    turtle.pencolor("Indigo")
    koch(300, 3)
    turtle.right(360 / 7)
    turtle.pencolor("Violet")
    koch(300, 3)
    turtle.hideturtle()
    turtle.done()

main()

