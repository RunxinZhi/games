import random

def introduction():
    print('''
Welcome to odd-ball game! You are given an even number
of balls, labelled, and among the balls one is heavier
than the rest, called the odd ball. 

Your goal is to find out which one is the odd one.
You are given a weighing scale!

Good Luck and have fun!
''')

def promptBallNumber():
    while True:
        try:
            # globalize the number of balls as "n"
            global n
            n = int(input("Enter the number of balls for the game?"))

            # check if there is an even number of balls
            1 / (n % 2 - 1)          

            # check if n is positive
            random.randint(1,n)  

            break
        except:
            print('''Invalid input!!!! 
            
Notice that you can only input a positive and EVEN integer.
Plz try again:''')

    # globalize the label of the oddball
    global oddBall
    oddBall=random.randint(1,n)

def promptWeigh():
    while True:
        print('''
You are prompted to enter the balls
to be placed on the pans of the scale,
separate each ball indentifier with one
minimum space, e.g. 1 2 3
''')

        l = input("Enter the ball identifier(s) to be placed on left pan:")
        r = input("Enter the ball identifier(s) to be placed on right pan:")

        try:
            # check if there is different numbers of balls in both pans
            ballsCount1=[]
            for i in range(len(l.split())):
                ballsCount1.append(i)
            for i in range(len(r.split())):
                ballsCount1.remove(i)

            ballsCount2=[]
            for i in range(len(r.split())):
                ballsCount2.append(i)
            for i in range(len(l.split())):
                ballsCount2.remove(i)

            # check if there is duplicate, or inexisting balls in the pans
            totalBalls = []
            for i in range(1,n+1):
                totalBalls.append(str(i))

            for i in l.split():
                totalBalls.remove(i) 
            for i in r.split():
                totalBalls.remove(i)

            # check if both pans are empty
            1 / len(l.split())
            1 / len(r.split())

            break
        except:
            print('Your inputs for left: "%s" ' % l, 'right: "%s" ' % r, end="\n")
            print('''Invalid input!!!!

Please ensure correct ball indentifiers (1-%s)
are entered on each pan, no duplicate balls on either
or both pans. Both pans should have the same number of
balls and must have at least one ball.
''' % n)
            
    scale = l.split() + r.split()
    return scale
        
def scaleOutput(scale):
    if str(oddBall) in scale[0:int(len(scale)/2)]:
        print("The scale shows: Left pan is down")
    elif str(oddBall) in scale[int(len(scale)/2):int(len(scale))]:
        print("The scale shows: Right pan is down")
    else:
        print("The scale shows: Both pans are balanced")

def promptGuess():
    guess = input("Enter the odd number or press Enter to weigh:")
    if guess.split() == [str(oddBall)]:
        print("Congratulations!!!! Your answer is correct.")
        return 1
    elif guess == "":
        return 0
    else:
        print("Your answer is incorrect!!!!")
        return 0

def startANewGame():
    anotherGame = input("Want a new game? -> Enter 1 if yes, and any other string to quit.")
    if anotherGame.split() == ['1']:
        return 1
    else:
        return 0

def oneSingleGame():
    introduction()
    promptBallNumber()
    scaleUsageCount = 0
    while True:
        scaleOutput(promptWeigh())
        scaleUsageCount += 1
        if promptGuess() == 1: # when the guess is correct
            print("Scale usage count: ", scaleUsageCount)
            return
        else:
            continue

def main():
    while True:
        oneSingleGame()
        if startANewGame() == 1: #when the player wants a new game
            continue
        else:
            print("Ok goodbye :)")
            break

main()