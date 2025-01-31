import random
import turtle

g_flip = []
g_colorSet = []

g_turtle = turtle.Turtle('square')
g_turtle.shapesize(2.5, 2.5, 3)
g_turtle.up()
g_turtle.hideturtle()

playboard = turtle.Screen()
playboard.setup(700,700)
playboard.tracer(0)

g_dim = 5
g_digit_range = 5
g_game = []

flip = []
prompt = []
tilts = []
coordinates = []

exitTile = turtle.Turtle('square')
exitTile.color("dark green")
exitTile.shapesize(2.5, 10, 0)
exitTile.goto(310, -310)
exitTile.stamp()

exitMessage = turtle.Turtle()
exitMessage.goto(260,-325)
exitMessage.write( arg = "Exit", move = True, font = ("Arial", 18, "normal"))

fromNumberToColor={0 : "red", 1 : "yellow", 2 : "blue", 3 : "green", 4 : "purple", 5 : "orange"}
fromColorToNumber={"red" : 0, "yellow" : 1, "blue" : 2, "green" : 3, "purple" : 4, "orange" : 5}

def createGame(dim, digit_range):
    b = []
    for _ in range(dim*dim):
        b.append(random.randint(0,digit_range))
    return b

g = createGame(g_dim, g_digit_range)

gameInstruction = turtle.Turtle()
gameInstruction.penup()
gameInstruction.goto( (-330, -300))
gameInstruction.pendown()
gameInstruction.write( arg = 
'''Welcome to FlipColor Game! Click any tile on the 5x5 playboard, and click any of the six colors 
presented in the color set. The color of the last tile you chose from the playboard will be changed 
into the first color you chose from the color set, and every neighbor of the chosen tile will change 
color as well. Your aim is to repeat the color changing process until all the tiles have been flipped 
into a same color.

Have fun!!!! (Click "Exit" to end)
''', move = True, align = 'left', font = ('Arial', 12, "normal") )

gameHint = turtle.Turtle()

def colorSet():

    color = ["red", "yellow", "blue", "green", "purple", "orange"]

    for i in range(6):
        g_turtle.penup()
        g_turtle.goto(-160 + 60 * i, -100)
        g_turtle.pen(pencolor = "black", fillcolor = color[i])
        g_turtle.stamp()
        g_colorSet.append([-160 + 60 * i, -100, color[i]])

def refreshScreen(game):
    
    g_flip.clear()

    for r in range(g_dim):
        for c in range(g_dim):

            screen_x = - 155 + 60 * c
            screen_y = 210 - 60 * r

            g_turtle.penup()
            g_turtle.goto(screen_x, screen_y)
            g_turtle.pendown()

            number = game[r*g_dim + c]
            color = fromNumberToColor[number]
            g_turtle.color(color)

            g_turtle.stamp()
            g_flip.append([screen_x, screen_y, g_turtle.fillcolor()])

def promptColorToFlip(x, y):
    global g
    for items in g_colorSet:

        # determine the color the player chose to flip to
        if items[0]-30 <= x < items[0]+30 and items[1]-30 <= y <= items[1]+30:
            flip.append(fromColorToNumber[items[2]])
            print(flip)
            
            try:
                print(tilts[-1])

                # recall the tile the player wants to flip
                col = int((tilts[-1][0] + 155) / 60)
                row = int((210 - tilts[-1][1]) / 60)
                orig = fromColorToNumber[tilts[-1][2]]
                print(row, col, orig, flip[-1])

                # flip the tile
                g = flipNumber(row, col, g, orig, flip[-1])
                print(g)
                refreshScreen(g)

            except: 
                pass

            return

        else:
            pass

def promptFlip(x, y):
    global g
    refreshScreen(g)

    coordinates.append([x, y])
    print(coordinates[-1])
    if len(coordinates) > 1:
        lastClick = coordinates[-2]
    else:
        lastClick = [700, 700]

    # calls when the player clicks on the color set
    if -220 <= x <= 170 and -130 <= y <= -70:

        # calls when the player keeps choosing color
        if -220 <= lastClick[0] <= 170 and -130 <= lastClick[1] <= -70:
            gameHint.goto((-300, 240))
            gameHint.write( arg = '''
You have already flipped the chosen tile!!!! 
Please choose another one to flip.
            ''', move = True, font = ("Arial", 18, "normal"))
            pass

        # flip the tile
        else:
            promptColorToFlip(x, y)

        return

    # calls when the player clicks on tiles
    elif -185 <= x <= 115 and -60 <= y <= 240:

        gameHint.clear()

        for items in g_flip:

            # determine the tile the player chose to flip
            if items[0]-30 <= x < items[0]+30 and items[1]-30 <= y < items[1]+30:
                tilts.append(items)
                col = int((tilts[-1][0] + 155) / 60)
                row = int((210 - tilts[-1][1]) / 60)
                print(row, col)

                idx = g_flip.index(items)
                g_turtle.penup()
                g_turtle.goto(g_flip[idx][0], g_flip[idx][1])
                g_turtle.pen(pencolor = "black", fillcolor = g_flip[idx][2])
                g_turtle.stamp()
                g_turtle.penup()

            else:
                pass

        # calls when all the tiles have been flipped into the same color
        if len( list( set(g) ) ) == 1:
            gameHint.penup()
            gameHint.goto((-300, 210))
            gameHint.pendown()
            gameHint.write ( arg = '''
You won!!!! Now you may choose any color you desire!!!!
            ''', move = True, font = ("Arial", 18, "normal") )

    # calls when the player clicks on the "exit" button
    elif 200 <= x <= 340 and -340 <= y <= -280:
        exit()

    else:
        pass

def flipNumber(row, col, game, orig, to):
    if orig == to:
        return game
    if row < 0 or row >= g_dim:
        return
    if col < 0 or col >= g_dim:
        return

    idx = row * g_dim + col   
    if game[idx] != orig:
        return
    
    game[idx] = to
    flipNumber(row-1, col, game, orig, to)
    flipNumber(row+1, col, game, orig, to)
    flipNumber(row, col-1, game, orig, to)
    flipNumber(row, col+1, game, orig, to)
    
    return game

if __name__ == "__main__":
    print(g)
    colorSet()
    refreshScreen(g)

    playboard.onscreenclick(promptFlip)

turtle.done()