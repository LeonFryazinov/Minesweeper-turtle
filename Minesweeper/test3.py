import turtle


screen = turtle.Screen()
t = turtle.Turtle()
t.color("black", "lime")
t.ht()

t.speed(0)
screen.tracer(0)
t.goto(0,0)
t.pensize(0)
t.down()
t.begin_fill()
t.circle(50)
t.end_fill()
screen.update()
screen.mainloop()