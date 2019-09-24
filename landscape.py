import turtle

luigi = turtle.Turtle()
koopa = turtle.Turtle()

khide = koopa.color("snow4")



def roadlines(i):
    for i in range (i):
        koopa.color("gold")
        koopa.forward(1)
        koopa.color("snow4")
        koopa.forward(2)
        koopa.color("gold")
        koopa.forward(2)



turtle.bgcolor("midnight blue")
luigi.color("midnight blue")
luigi.right(90)
luigi.forward(45)
luigi.color("green")
luigi.begin_fill()
luigi.right(270)
luigi.forward(500)
luigi.right(90)
luigi.forward(500)
luigi.right(90)
luigi.forward(1000)
luigi.right(90)
luigi.forward(500)
luigi.right(90)
luigi.forward(500)
luigi.end_fill()
luigi.color("snow4")
luigi.begin_fill()
luigi.right(45)
luigi.forward(500)
luigi.right(135)
luigi.forward(750)
luigi.right(135)
luigi.forward(500)
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
roadlines(100)






















turtle.exitonclick()
