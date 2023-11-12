import turtle

# wn
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("My initials")
wn.setup(800, 600)

# t
t = turtle.Turtle()
t.shape("turtle")
t.shapesize(2)
t.pensize(5)
t.pencolor("black")
t.speed(5)
t.penup()
t.left(180)
t.forward(50)
t.pendown()
t.right(45)
t.forward(70)
t.right(180)
t.forward(70)
t.left(90)
t.forward(70)
t.right(180)
t.forward(70)
t.left(45)
t.forward(50)
t.penup()
t.left(90)

for i in range(2):
    if i == 0:
        t.forward(75)  # move to the next letter
    else:
        t.forward(30)

    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(60)
    t.penup()
    t.right(90)
    t.forward(100)
    t.left(90)


wn.mainloop()
