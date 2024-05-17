import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(30)

turtle.bgcolor("black")
for i in range(37960):
	t.color("lime")
	t.circle(i)
	t.left(900)
	t.right(90)

turtle.done()