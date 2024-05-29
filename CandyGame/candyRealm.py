# Name: Taylor Bauer            Date: 2023-11-22
# Assignment VI
# Description: This is a game remnant of Candy Land using the turtle module for the main visual aspect of moving pieces and card drawing. The board squares correspond to a set of coordinates contained within a dictionary.

# TODO: Student turns in their assignment before the 11:59 p.m. Friday deadline and the file is named candyRealm.py
#       (delete this TODO line when completed) (1 pt.)

import turtle
import random
import pyfiglet

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number using pyfiglet."""
    
    try:  
        print(pyfiglet.figlet_format("Candy Game !", font="slant"))
        print("By: Taylor Bauer")
        print("[COM S 127 Section: G]")
    
    except ImportError: 
        print("""
Candy Game!
          
By: Taylor Bauer
          
[COM S 127 Section: G]""")
        print("I used the PyFiglet module for the Title - you may need to install it.")

def theCandyBoard(wn):
    """This function changes the background canvas to a board created on Canva."""
    
    wn.setup(width=500, height=500)
    wn.bgcolor("#B1A1ED")
    wn.bgpic("candy.gif")

def gameMenu():
    """This function is for the game menu choices"""
    
    print("""
Hello! Welcome to 'Candy Realm' or as I like to call it 'Candy Game.'

You are currenlty in game menu with the following options.

> 1. Start Candy Realm

> 2. Instructions for Candy Realm

> 3. Quit\n""")
    while True:  
        try:
            choice = int(input("""Please select which one you would like to do: """))
            
            if choice not in [1, 2, 3]:
                print("""
    ERROR: Apologies for the confusion, you must select one of the following:
                    
    > 1. Start Candy Realm
                    
    > 2. Instructions for Candy Realm
                    
    > 3. Quit""")
            
            else:
                return choice
        
        except ValueError:
            print("\nApologies, I cannot accept your input! Are you entering a number?")

def theInstructions():
    """This functions defines the instructions of the game upon confusion."""
    
    instructions = [
        "The Candy Realm Game is as follows:",
        "Rule I: To determine each player - Player 1 will be the youngest, type in your name and following players also correspond with order of age. Sadly, no computer player",
        "Rule II: For each turn - the current player chooses a card.",
        "Rule III [The Cards]: For a single color card (one square) - the player will move forward one square matching the card color. For a card with the same two colors (two squares) - the player will move forward two squares matching the card color. For a card with two different colors (two squares) - the player will be skipped, losing a turn.",
        "Rule IV [Winning]: To win - the player must draw a green card marking the finish (single or two) landing them on the square.",
        "Rule V: I'm not going to implement this into the game to enforce it; however, if you gave no more remaining moves before reaching the green... You must move background the square amount on your drawing turn"
        "Rule VI: Have fun with my sadly implemented candy game! ~ The Creator"
    ]

    print("\nContinously press [enter] for the rules!\n")
    
    for z in instructions:
        print(z)
        input("")

def cardColors(): 
    """This function is the list of colors in the game!"""
    
    colors_list = ["#C2FFC1","#FF7575", "#6E6CFF","#BA60D4","#FFC8F3", "#FFFEA5"]
    
    return colors_list

def stuartDrawSquare(xcor, ycor, color, turt):
    """This function uses a turtle to draw a square for the cards."""
    
    turt.goto(xcor, ycor) 
    turt.pendown()
    turt.fillcolor(color)
    turt.pencolor(color)
    turt.begin_fill()
    
    for z in range(4):
        turt.forward(60)
        turt.right(90)
    
    turt.end_fill()
    turt.penup()

def singleSquareCard(colors, turt):
    """This function draws a single square color card with a turtle 
       and a randomly generated color from the colors list."""
    
    turt.clear()

    color = random.choice(colors)
    
    turt.penup()
    turt.hideturtle()

    stuartDrawSquare(130, 240, color, turt)

def twoSquareCard(colors, turt):
    """This function draws a two square color card with a turtle
       and randomly generated colors from the colors list."""
    
    turt.clear()
    
    color_1 = random.choice(colors)
    color_2 = random.choice(colors)

    turt.penup()
    turt.hideturtle()

    stuartDrawSquare(130, 240, color_1, turt)

    stuartDrawSquare(70, 240, color_2, turt)

    return color_1, color_2

def displayCard(colors, turt):
    """This function uses condtional logic to draw a card from the list. 
        Within the list there are multiple of the same type to adjust the 
        probabilty of a card being drawn. Additonally, this function implements
        the skip logic, skipping a player if a card of two different colors
        is drawn. Furthermore, it displays a message with the corresponding card."""
    
    card_types = ["single", "single", "single", "single", "same_two", "same_two", "same_two", "same_two", "different_two"]
    card = random.choice(card_types)
    
    turt.clear()
    turt.speed("fastest")

    skip = False

    if card == "single":
        singleSquareCard(colors, turt)
        show = "Wohoo! Great! You get to move forward one square!"
        display(turt, show)

    elif card == "same_two" or card == "different_two":
        color_1, color_2 = twoSquareCard(colors, turt)
        
        if color_1 is color_2:
            show = "Wohoo! Great move forward two squares!" 
            display(turt, show)

        else:
            show = "Uh oh. Two separate colors :(. Skip turn lol"
            display(turt, show)
            skip = True
    
    return card, skip

def display(turt, display):
    """This function moves the turtle to display the message with the card"""

    turt.color("#000000")
    turt.goto(- 230, 200)
    turt.write(display, align="left", font=("Verdana", 10))

def numberPlayers():
    """This function uses input validation for the number of players in the game.
    Users must choose between 2 - 4 players, limit cannot be exceeded or under.
    Players do not have the option of playing with computer due to creators poor time management skills."""
    
    while True:
        try:
            number_players = int(input("How many players will be joining 'Candy Game' today? '2', '3', or '4': "))
            
            if number_players < 2 or number_players > 4:
                print("ERROR: Apologies for the confusion, there must be 2 - 4 players.")

            else:
                return number_players
        
        except ValueError:
            print("\nApologies, I cannot accept your input! Are you entering a number?")

def thePlayers(number_players):
    """This function assigns the players with their corresponding 
       images, start positions, and name for each player entered."""
    
    images = ["player_1.gif", "player_2.gif", "player_3.gif", "player_4.gif"]
    
    players = []
    
    starting = [(- 215, - 140), (- 180 ,- 125), (- 210, - 180), (- 175, - 190)]
    
    for z in range(number_players):
        turtle.register_shape(images[z])
        
        player = turtle.Turtle()
        player.shape(images[z])
        player.penup()
        
        name = input(f"Yahoo competitor {z + 1}! Would you mind entering your name: ")
        
        player.goto(starting[z])
        
        players.append((player, name))
    
    return players

def userInput(coordinates):
    """This function recieves input from player for a square number."""    
    
    while True:
        try:
            square = int(input("Please enter the square number you must move to: "))
            
            if square in coordinates:
                return square
            
            else:
                print("Apologies for the confusion! You must enter your number of the square contained within the board!")
        
        except ValueError:
            print("\nApologies, I cannot accept your input! Are you entering a number?")

def nextPlayer(present_player, num_players, pieces):
    """This function is for the next player."""

    present_player = (present_player + 1) % num_players
    
    name = pieces[present_player][1]
    
    print(f"\nMoving on, it's {name}'s turn! Press [enter] to continue...")
    input()

    return present_player


def playerMove(player, square, coordinates, turt):
    """This function moves the player to the correct board square based on input using a dictionary.
       Additonally, if the player lands on one of the 'Cool Square' coordinates, they move upwards
       and a message is shown."""
    
    cool_squares = {10:35, 17:28}
    
    turt.penup()
    
    if square in cool_squares:
        player.goto(coordinates[square])
        new_square = cool_squares[square]
        player.goto(coordinates[new_square])
        
        turt.goto(player.position())
        turt.write("Slayy!! Bridge shortcut!", align="right", font=("Verdana", 10))
    
    elif square in coordinates:
        player.goto(coordinates[square])
    
    else:
        print("Apologies! There must be something wrong! There has been an error!")

def checkForWin(player, coordinates, square, turt):
    """This function checks for a winner in the game and draws the winner stuff."""

    if square == 48:
        turt.clear()
        turt.hideturtle()
    
        player.goto(coordinates[49])

        winStuff(turt)
        
        return True

    return False

def confetti(turt):
    """This function draws random confetti after a win!!"""
    
    turt.speed("fastest")
    turt.pensize(3)
    turt.penup()

    for z in range(100):
        
        x = random.randint(- 250, 250)
        y = random.randint(- 250, 250)
        turt.goto(x, y)

        x += random.randint(- 20, 20)
        y += random.randint(- 20, 20)

        turt.pencolor(random.choice(["#FFD700", "#FF69B4", "#1E90FF", "#FF8C00", "#32CD32", "#9932CC"]))
        
        turt.pendown()
        turt.goto(x, y)
        turt.penup()

def displayWinner(turt):
    """This function shows a message to the winner after a win. """
    
    turt.hideturtle()
    turt.penup()
    
    turt.goto(0, 100)
    
    turt.pencolor("#000000")
    turt.write("SLAY WINNA!", align="center", font=("Arial", 40, "bold"))

def smiley(turt):
    """This function draws a smiley after a win!"""
    
    turt.hideturtle()
    turt.speed("fastest")
    
    turt.penup()
    turt.goto(0, 0)
    turt.pendown()
    turt.circle(50)

    turt.penup()
    turt.goto(- 20, 60)
    turt.pendown()
    turt.dot(10)

    turt.penup()
    turt.goto(20, 60)
    turt.pendown()
    turt.dot(10)

    turt.penup()
    turt.goto(- 33, 45)
    turt.pendown()
    turt.right(90)
    turt.circle(33, 180)
    turt.hideturtle()

def gameOva(turt):
    """This function displays game over after a win."""
    
    turt.hideturtle()
    turt.penup()

    turt.goto(0, - 70)

    turt.pencolor("#000000")
    turt.write("Game Ova!", align="center", font=("Arial", 30, "bold"))


def winStuff(turt):
    """"This function calls all of the previous win stuff and displays it."""
    
    confetti(turt)
    displayWinner(turt)
    smiley(turt)
    gameOva(turt)

def main():
    """This function is where all the fun happens! """

    # these are my board coordinates, sorry lol
    
    coordinates = {
    1: (- 135, - 160), 2: (- 98, - 160), 3: (- 61, - 160), 4: (- 24, - 160), 5: (14, - 160),
    6: (52, - 160), 7: (90, - 160), 8: (128, - 160), 9: (128, - 122), 10: (128, - 84),
    11: (90, - 84), 12: (52, - 84), 13: (14, - 84), 14: (14, - 46), 15: (14, - 8),
    16: (- 24, - 8), 17: (- 61, - 8), 18: (- 61, - 46), 19: (- 61, -84), 20: (- 98, - 84),
    21: (- 135, - 84), 22: (- 172, - 84), 23: (- 172, - 46), 24: (-172, -8), 25: (- 172, 29),
    26: (- 172, 66), 27: (- 135, 66), 28: (- 98, 66), 29: (- 61, 66), 30: (- 24, 66),
    31: (14, 66), 32: (52, 66), 33: (89, 66), 34: (89, 29), 35: (89, - 8),
    36: (128, - 8), 37: (165, - 8), 38: (165, 29), 39: (165, 66), 40: (165, 103),
    41: (175, 150), 42: (127, 140), 43: (89, 140), 44: (51, 140), 45: (14, 140),
    46: (- 23, 140), 47: (- 60, 140), 48: (- 97, 140), 49: (- 134, 140)
  }
    
    # tile
    printTitleMaterial()

    # game loop variable
    running = True

    while running:       
        
        # game choice
        choice = gameMenu()

        if choice == 1:

            # settin' up the game window
            candy_window = turtle.Screen()
            theCandyBoard(candy_window)

            # game stuff i.e., cards, turtles
            colors = cardColors()
            stuart = turtle.Turtle()
            stuart.hideturtle()

            # players
            num_players = numberPlayers()
            pieces = thePlayers(num_players)

            # index for the player currently playing
            present_player = 0

            # game commencement variable
            game = True
            
            # wina variable! 
            win = False

            # while the game goin'
            while game:

                # the game piece and name gathering
                player, name = pieces[present_player]

                # player draw card >:)
                print(f"> {name}, you're up! Press [enter] to draw a card...")
                input()

                # cards and turn skip unpacking
                card, skip = displayCard(colors, stuart)

                # skips n game action!!!
                if not skip:
                    square = userInput(coordinates)
                    playerMove(player, square, coordinates, stuart)
                    win = checkForWin(player, coordinates, square, stuart)

                    if win:
                        print(f"\nYEEEHAWWW {name}! You've won the game by reaching the 'WINNER RAINBOW!'")
                        input("Press [enter] to leave the Candy Realm...")
                        print("Goodbye! We hope to see you next time in the Candy Realm!")
                        quit()

                else:
                     print(f"OH NO, {name}! Your turn is skipped because of two different card colors.")
            
                # next player!!!! lets gooo!
                present_player = nextPlayer(present_player, num_players, pieces)

            candy_window.mainloop()
        
        elif choice == 2:
            theInstructions()
        
        elif choice == 3:
            print("Goodbye! We hope to see you next time in the Candy Realm!")
            break
        
        else:
            print("Apologies! There must be something wrong! You will now be leaving the Candy Realm...")
            quit()

if __name__ == "__main__":
    main()