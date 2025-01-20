import turtle as t
import random
import time
maze=t.Screen()
maze.setup(700,700)
maze.bgcolor("black")
maze.title('Pac-Man')
maze.tracer(0)

levels=[]
level_1=[
    "XXXXXXXXXXXXXXXXXXX",
    "XCCCC  D XCCCCCCC X",
    "XCXXX XX  CXXCXXX X",
    "X   X XXCX XXCX   X",
    "X X CCCCCX   C  X X",
    "X XXXXCXXXXX XXXX X",
    "X   CCC  X       DX",
    "XCXX  XX X XXCCXX X",
    "XCCC  X     X CCCCX",
    "XXX XXX XXX XXXCXXX",
    "XXX    PXXX    CXXX",
    "XXX XX  XXX  XXCXXX",
    "X   X         XCCCX",
    "X XXX XX X XX XXXCX",
    "X   X    X    XCCCX",
    "XXX X XXXXXXX XCXXX",
    "X        D  CCCC  X",
    "X XXX XXCXCXX XXX X",
    "X   X XXCXCXX X   X",
    "XXX DCCCCXCCCC  XXX",
    "XXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)

score=0
life=3
walls=[]
golds=[]
devils=[]
words=[]

class Devil(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.shape("triangle") 
        self.shapesize(1)
        self.color("purple")
        self.speed(0)
        self.penup
        self.fx=random.choice(['Up','Down','Right','Left'])

    def rules(self,go_x,go_y):
        if (go_x,go_y) not in walls:
            self.goto(go_x,go_y)
            maze.update()

    def moveDevil(self):
        self.fx=random.choice(['Up','Down','Right','Left'])
        if self.fx=='Up':
            i=0
            for i in range(random.randint(0,5)):
                go_x=self.xcor()
                go_y=self.ycor()+24
                self.rules(go_x,go_y)
                time.sleep(0.06)
                i=i+1
        elif self.fx=='Down':
            i=0
            for i in range(random.randint(0,5)):
                go_x=self.xcor()
                go_y=self.ycor()-24
                self.rules(go_x,go_y)
                time.sleep(0.06)
                i=i+1
        elif self.fx=='Right':
            i=0
            for i in range(random.randint(0,5)):
                go_x=self.xcor()+24
                go_y=self.ycor()
                self.rules(go_x,go_y)
                time.sleep(0.06)
                i=i+1
        elif self.fx=='Left':
            i=0
            for i in range(random.randint(0,5)):
                go_x=self.xcor()-24
                go_y=self.ycor()
                self.rules(go_x,go_y)
                time.sleep(0.06)
                i=i+1
        t.ontimer(self.moveDevil,random.randint(500,700))

class Gold(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.shape("circle")
        self.shapesize(0.1)
        self.color("lightskyblue")
        self.speed(0)
        self.penup

class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.speed(0)
        self.shape("circle")
        self.color("yellow")

    def look_for_gold(t,self):
        global score 
        for g in golds:
            if g.distance(player)==0:
                score=score+1
                g.hideturtle()
                golds.remove(g)
                scoreValue.clear()
                Value(scoreValue,score,"blue",300,270)
                if score==63:
                    scoreValue.clear()
                    Background()
                    Value(scoreValue,"You Win!","black",0,0)

    def touching_devils(t,self):
        global life
        for d in devils:
            if d.distance(player)<=25:
                life=life-1
                lifeValue.clear()
                Value(lifeValue,life,"red",-220,270)
                if life==0:
                    lifeValue.clear()
                    Background()
                    Value(lifeValue,"You Lose","black",0,0)

    def move(self,go_x,go_y):
        if (go_x,go_y) not in walls:
            self.goto(go_x,go_y)
            maze.update()
            self.look_for_gold(t)
            self.touching_devils(t)

    def go_right(self):
        go_x=self.xcor()+24
        go_y=self.ycor()
        self.move(go_x,go_y)

    def go_left(self):
        go_x=self.xcor()-24
        go_y=self.ycor()
        self.move(go_x,go_y)

    def go_up(self):
        go_x=self.xcor()
        go_y=self.ycor()+24
        self.move(go_x,go_y)

    def go_down(self):
        go_x=self.xcor()
        go_y=self.ycor()-24
        self.move(go_x,go_y)

class Pen(t.Turtle):
    def __init__(self): #__init__:initiate pen
        super().__init__() #initiate turtle (variables in class also need to initiate)
        self.hideturtle()
        self.speed(0)
        self.shape("square")
        self.color("brown")
        self.penup()
        self.goto(200,200)
        self.showturtle()

    def make_maze(self,level):
        for i in range(len(level)):
            row=level[i]
            for j in range(len(row)):
                screen_x=-220+24*j
                screen_y=-240+24*i
                char=row[j]
                if char=='X':
                    self.goto(screen_x,screen_y)
                    self.stamp()
                    walls.append((screen_x,screen_y)) #tuple
                elif char=='P':
                    player.goto(screen_x,screen_y)
                    player.showturtle()
                elif char=='C':
                    gold=Gold()
                    golds.append(gold)
                    gold.goto(screen_x,screen_y)
                    gold.showturtle()
                elif char=='D':
                    devil=Devil()
                    devils.append(devil)
                    devil.goto(screen_x,screen_y)
                    devil.showturtle()

pen=Pen()
player=Player()
pen.make_maze(level_1)

lifeString=t.Turtle()
scoreString=t.Turtle()
lifeValue=t.Turtle()
scoreValue=t.Turtle()
background=t.Turtle()

def Message(String,content,color,CoX,CoY):
    String.ht()
    String.speed(0)
    String.penup()
    String.goto(CoX,CoY)
    String.color(color)
    String.write(content,font=("Arial","20"))

def Value(Value,content,color,CoX,CoY):
    Value.ht()
    Value.speed(0)
    Value.penup()
    Value.goto(CoX,CoY)
    Value.color(color)
    Value.write(content,font=("Arial","20"))

def BackgroundRectangle():
    background.forward(600)
    background.right(90)
    background.forward(100)
    background.right(90)
    background.forward(600)
    background.right(90)
    background.forward(100)

def Background():
    background.ht()
    background.speed(0)
    background.penup()
    background.goto(-300,70)
    background.pendown()
    background.color("green")
    background.begin_fill()
    BackgroundRectangle()
    background.end_fill()

Message(lifeString,"life=","red",-270,270)
Message(scoreString,"score=","blue",200,270)
Value(lifeValue,life,"red",-220,270)
Value(scoreValue,score,"blue",290,270)

maze.listen()
maze.onkey(player.go_right,'Right')
maze.onkey(player.go_left,'Left')
maze.onkey(player.go_up,'Up')
maze.onkey(player.go_down,'Down')

for d in devils:
    t.ontimer(d.moveDevil,random.randint(0,1))
    maze.update()

maze.mainloop()