import turtle


mario = turtle.Turtle
luigi = turtle.Turtle()
koopa = turtle.Turtle()

khide = koopa.color("snow4")


def basic(i):
    for i in range (i):
        mario.forward(i)
        mario.right(270)
        mario.forward(i+100)
        mario.right(270)
        mario.forward(i)
        mario.right(270)
        mario.forward(i+100)
        mario.right(270)
        mario.forward(i)


def roadlines(i):
    for i in range (i):
        koopa.color("gold")
        koopa.forward(i+1)
        koopa.color("snow4")
        koopa.forward(i+1)
        koopa.color("gold")
        koopa.pensize(i+1)



turtle.bgcolor("midnight blue")
luigi.color("midnight blue")
luigi.right(90)
luigi.forward(45)
luigi.color("green")
luigi.begin_fill()
luigi.right(270)
luigi.forward(1000)
luigi.right(90)
luigi.forward(1000)
luigi.right(90)
luigi.forward(2000)
luigi.right(90)
luigi.forward(1000)
luigi.right(90)
luigi.forward(1000)
luigi.end_fill()
luigi.color("snow4")
luigi.begin_fill()
luigi.right(45)
luigi.forward(750)
luigi.right(135)
luigi.forward(1100)
luigi.right(135)
luigi.forward(750)
luigi.right(45)
luigi.forward(50)
luigi.end_fill()
koopa.color("midnight blue")
koopa.right(90)
koopa.forward(45)
koopa.right(90)
koopa.color("snow4")
koopa.forward(25)
koopa.right(270)
koopa.speed(900)
roadlines(20)

basic(50)





















turtle.exitonclick()
