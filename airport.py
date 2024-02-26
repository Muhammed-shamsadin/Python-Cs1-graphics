from cs1graphics import*
from time import*
import time

canvas=Canvas(1000,650,"light blue", "Bole Internatonal Airport")

#sky
sunall=Layer()
sun = Circle(30,Point(1000,200))
sun.setDepth(70)
canvas.add(sun)
sun.setFillColor("yellow")

moon = Circle(30, Point(-30,200))
moon.setDepth(70)
moon.setFillColor("white")
canvas.add(moon)


text=Text('BOLE INTERNATIONAL AIRPORT', 15, Point(126,290))
text.setDepth(40)
text.setFontColor('black')
canvas.add(text)


  
#AIRPLANE
plane=Layer()
def add_plane(plane,x,y):
    plane.moveTo(x,y)
    e=Ellipse(150,40, Point(0,0))
    e.setFillColor("Orange")
    e.setBorderColor('white')
    e.setBorderWidth(2)
    plane.add(e)

    a=Point(58,-13)
    b=Point(61,10)
    nose=Spline(a,b)
    nose.setBorderWidth(2)
    plane.add(nose)

    tail=Polygon(Point(-75,-3), Point(-90,-45), Point(-64,-55), Point(-57,5))
    tail.setFillColor("red")
    tail.setBorderColor("white")
    tail.setDepth(51)
    tail.setBorderWidth(2)
    plane.add(tail)

    wing=Polygon(Point(5,-21), Point(-10,-40), Point(-15,-25),Point(-12,-20))
    wing.scale(1.5)
    wing.setFillColor('red')
    wing.setBorderWidth(2)
    wing.setBorderColor('white')
    wing.setDepth(51)
    plane.add(wing)

    wing2=wing.clone()
    wing2.moveTo(2,20)
    wing2.setFillColor('red')
    wing2.flip(1)
    wing2.rotate(180)
    wing2.setDepth(51)
    wing2.setBorderColor('white')
    plane.add(wing2)
    plane.setDepth(5)
    canvas.add(plane)
    plane.rotate(-47)


#Road
Asphalt=Polygon(Point(730,250),Point(300,650),Point(750,650),Point(870,250))
Asphalt.setBorderWidth(4)
Asphalt.setDepth(52)
Asphalt.setFillColor("black")
Asphalt.setBorderColor("white")
canvas.add(Asphalt)

#ZEBRA
z1=Path(Point(530,650),Point(595,550))
z1.setBorderWidth(14)
z1.setBorderColor("white")
canvas.add(z1)

z2=Path(Point(625,500),Point(687,400))
z2.setBorderWidth(13)
z2.setBorderColor("white")
canvas.add(z2)

z3=Path(Point(720,350),Point(763,280))
z3.setBorderWidth(12)
z3.setBorderColor("white")
canvas.add(z3)
z4=Path(Point(530,650),Point(595,550))
z4.setBorderWidth(15)
z4.setBorderColor("white")
canvas.add(z4)




#LAND
bx=Polygon(Point(1000,250),Point(0,250),Point(0,650),Point(1000,650))
bx.setBorderWidth(3)
bx.setFillColor('dark green')
bx.setDepth(70)
canvas.add(bx)

#TREES
def trees(x,y):
    tree = Layer()
    tree_top = Polygon(Point(0,0),Point(30,60),Point(20,60),Point(30,80),
                   Point(20,80),Point(30,110), Point(-30,110),Point(-20,80),
                Point(-30,80),Point(-20,60),Point(-30,60))
    tree.moveTo(x,y)
    tree_top.setFillColor("springgreen4")
    tree_bottom = Rectangle(15,40,Point(0,130))
    tree_bottom.setFillColor("firebrick")
    tree.add(tree_top)
    tree.add(tree_bottom)
    tree.setDepth(10)
    tree.scale(0.5)
    canvas.add(tree)


trees(450,210)
trees(500,210)
trees(550,210)
trees(600,210)
trees(650,210)
trees(450,300)
trees(500,300)
trees(550,300)

trees(890,210)
trees(950,210)
trees(890,300)
trees(950,300)
trees(890,390)
trees(950,390)
trees(890,480)
trees(950,480)
trees(890,570)
trees(950,570)
trees(890,650)
trees(950,650)






#cloud
def cloud(mmm,yyy):
    clouds=Layer()
    rctngl=Rectangle(100,40,Point(400,300))
    rctngl.setBorderColor("white")
    rctngl.setFillColor("white")
    s1=Ellipse(100,40,Point(400,300))
    clouds.add(rctngl)
    crcl=Circle(20,Point(350,300))
    clouds.add(crcl)
    crcl.setBorderColor("white")
    crcl.setFillColor("white")
    crcl2=crcl.clone()
    crcl2.moveTo(450,300)
    clouds.add(crcl2)
    crcl3=Circle(33,Point(418,275))
    clouds.add(crcl3)
    crcl3.setBorderColor("white")
    crcl3.setFillColor("white")
    crcl4=Circle(20,Point(370,280))
    clouds.add(crcl4)
    crcl4.setBorderColor("white")
    crcl4.setFillColor("white")
    clouds.scale(0.6)
    clouds.move(mmm,yyy)
    clouds.setDepth(500)
    clouds.scale(0.9)
    canvas.add(clouds)
cloud(780,-100)
cloud(580,-100)
cloud(550,-100)
cloud(220,-100)
cloud(180,-100)
cloud(-60,-100)

#Hill
mount=Layer()
hill1=Polygon(Point(700,250),Point(1100,100),Point(1170,180),Point(1300,30),Point(1500,250))
hill1.setFillColor('chocolate')
hill1.setBorderColor("black")
hill1.setBorderWidth(3)
hill1.setDepth(50)
hill1.scale(0.5)
canvas.add(hill1)

hill2=Polygon(Point(0,250),Point(150,100),Point(250,200),Point(350,65),Point(500,250))
hill2.setFillColor('Chocolate')
hill2.setBorderColor('black')
hill2.setBorderWidth(3)
hill2.scale(0.5)
hill2.setDepth(60)
canvas.add(hill2)



#BUILDING

block=Layer()

block1=Polygon(Point(100,350), Point(50,440), Point(50,630), Point(350,400), Point(350,300),Point(380,250))
block1.setFillColor("lightseagreen")
block1.setBorderWidth(3)
block.add(block1)

line=Path(Point(50,440),Point(350,300))
line.setBorderWidth(3)
block.add(line)

roof1=Polygon(Point(380,250),Point(0,275), Point(0,275), Point(0,330),Point(100,350))
roof1.setBorderWidth(4)
roof1.setFillColor("darkslategray2")
block.add(roof1)

side=Polygon(Point(0,605),Point(50,630), Point(50,440),Point(100,350), Point(0,330))
side.setBorderWidth(3)
side.setFillColor('lightskyblue4')
block.add(side)

line2=Path(Point(0,425), Point(50,440))
line2.setBorderWidth(3)
block.add(line2)


stripe1=Path(Point(115,345),Point(60,435), Point(60,622))
block.add(stripe1)
stripe2=Path(Point(140,335),Point(85,425),Point(85,606))
block.add(stripe2)
stripe3=Path(Point(168,325),Point(105,415),Point(105,590))
block.add(stripe3)
stripe4=Path(Point(195,315),Point(125,405),Point(125,575))
block.add(stripe4)
stripe5=Path(Point(223,305),Point(150,395),Point(150,555))
block.add(stripe5)
stripe6=Path(Point(252,295),Point(175,383),Point(176,533))
block.add(stripe6)
stripe7=Path(Point(252,295),Point(280,330),Point(280,453))
block.add(stripe7)
stripe8=Path(Point(268,292),Point(299,326),Point(299,439))
block.add(stripe8)
stripe9=Path(Point(288,285),Point(316,318),Point(316,428))
block.add(stripe9)
stripe10=Path(Point(305,278),Point(329,310), Point(329,418))
block.add(stripe10)

floor=Path(Point(50,480),Point(350,330))
floor.setBorderWidth(3)
block.add(floor)
floor2=Path(Point(50,565),Point(350,365))
floor2.setBorderWidth(3)
block.add(floor2)

door=Polygon(Point(200,420),Point(200,515),Point(270,461),Point(270,380))
door.setBorderWidth(4)
door.setFillColor('light yellow')
block.add(door)

canvas.add(block)



#MAN
Man=Layer()
head=Circle(6,Point(350,145))
head.setFillColor("black")
Man.add(head)
body=Rectangle(15,20, Point(350,163))
body.setFillColor("red")
Man.add(body)
hand1=Path(Point(345,153),Point(338,168))
hand1.setBorderWidth(4)
Man.add(hand1)
hand2=Path(Point(355,153),Point(362,168))
hand2.setBorderWidth(4)
Man.add(hand2)
leg1=Rectangle(5,13, Point(346,180))
leg1.setFillColor("black")
Man.add(leg1)
leg2=Rectangle(5,13, Point(354,180))
leg2.setFillColor("black")
Man.add(leg2)
Man.setDepth(10)
Man.moveTo(-110,450)
canvas.add(Man)
Man2=Man.clone()
Man2.moveTo(-130,330)
Man2.setDepth(10)
canvas.add(Man2)




#PLANES CALLED
Plane1 = Layer()
add_plane(Plane1,580,580)

Plane2=Layer()
add_plane(Plane2,580,710)

Plane3=Layer()
add_plane(Plane3,900,-70)
Plane3.rotate(95)
Plane3.flip()
Plane3.scale(0.15)
'''

         #ANIMATIONS    
canvas.setAutoRefresh(False)

a = 0
b = 0
c = -110
d = 5
e = 0
f = 0
g = 110
h = -5

for i in range(1550):
    Plane1.move(0.2,-0.39)
    if i % 100 == 0:
        Plane1.scale(0.95)
    if i < 1550:
        Man.move(0.01, -0.09)
        if i == 1549:
            canvas.remove(Man)
    canvas.refresh()

for i in range(6):
    sun.move(a,b)
    time.sleep(1)
    a = a-20
    b = b-8
    canvas.refresh()

for i in range(2000):
    Plane2.move(0.2,-0.39)
    if i % 100 == 0:
        Plane2.scale(0.95)
    canvas.refresh()

for i in range(6):
    sun.move(c, d)
    time.sleep(1)
    c = c - 15
    d = d + 5
    canvas.refresh()
    
canvas.setBackgroundColor("dark blue")

for i in range(6):
    moon.move(e, f)
    time.sleep(1)
    e = e+20
    f = f-8
    canvas.refresh()

for i in range(1700):
    Plane3.move(-0.2,0.39)
    if i % 100 == 0:
        Plane3.scale(1.1112)
    if i < 1550:
        Man2.move(-0.01, 0.09)
        if i == 1549:
            canvas.remove(Man2)
    canvas.refresh()

for i in range(6):
    moon.move(g,h)
    time.sleep(1)
    g= g+15
    h= h+5
    canvas.refresh()

'''
#CLOSING 

canvas.clear()
canvas.setBackgroundColor("black")
canvas.setAutoRefresh(False)

names=Layer()
names.move(500,700)
title = Text("BOLE INTERNATIONAL AIRPORT", 40,Point(0,0))
heading = Text("Group Members",30,Point(0,60))
name1 = Text("Muhammed Samson     UGR/26320/14",20,Point(0,100))
name2 = Text("Kalkidan Kidane     UGR/25274/14",20,Point(0,140))
name3 = Text("Mulgeta Negasa      UGR/25479/14",20,Point(0,180))
name4 = Text("Muse Zewude         UGR/25761/14",20,Point(0,220))
name5 = Text("Abraham Gashaw      UGR/26249/14",20,Point(0,260))
name6 = Text("Wasil Shukre        UGR/26399/14",20,Point(0,300))
name7 = Text("Eyerusalem Ayalew   UGR/26556/14",20,Point(0,340))
ending = Text("THANKS FOR WATCHING ",40,Point(0,420))
title.setFontColor("white")
heading.setFontColor("white")
name1.setFontColor("white")
name2.setFontColor("white")
name3.setFontColor("white")
name4.setFontColor("white")
name5.setFontColor("white")
name6.setFontColor("white")
name7.setFontColor("white")
ending.setFontColor("white")
names.add(title)
names.add(heading)
names.add(name1)
names.add(name2)
names.add(name3)
names.add(name4)
names.add(name5)
names.add(name6)
names.add(name7)
names.add(ending)
canvas.add(names)

for i in range(6000):
    names.move(0,-0.1)
    canvas.refresh()


    
