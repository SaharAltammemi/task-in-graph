import turtle
v=turtle.Turtle()
colors=['red','purple','blue','green','orange','yellow']
for x in range(100):
    v.pencolor(colors[x%6])
    v.forward(x)
    v.left(59)
turtle.done()