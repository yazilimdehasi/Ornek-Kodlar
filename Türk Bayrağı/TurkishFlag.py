import turtle
isaretci=turtle.Turtle()
isaretci.screen.setup(width=1000,height=550)
isaretci.speed(0)
isaretci.screen.bgcolor("red")
isaretci.hideturtle()
def konumla_boya(renk,yatay,dikey):
    isaretci.penup()
    isaretci.goto(yatay,dikey)
    isaretci.pendown()
    isaretci.color(renk)
    isaretci.begin_fill()

def star(boy):
    konumla_boya("white",77,64)
    for i in range(5):
        if i ==0:
            derece=125
        else:
            derece=144
        isaretci.right(derece)
        isaretci.forward(boy)
    isaretci.end_fill()

def daire(cap):
    isaretci.circle(cap)
    isaretci.end_fill()

konumla_boya("white", -175, -130)
daire(150)
konumla_boya("red", -140, -99)
daire(120)

star(130)

isaretci.screen.mainloop()
