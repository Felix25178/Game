import random


def instructions():
    print("""
    
    _____________________
    :::::::::::::::::::::
    {WELCOME TO GEOPARDY}
    *********************
    _____________________
    
    In this game you will choose a category and then answer a question in the category of your choosing.
    If you get it right you will be awarded points, get enough points and you win.
    
    Lets begin
    """)



def options():

    print(""" 
    ===================
    |CHOOSE A CATEGORY|
    -------------------
    
        History
        Math
        Animals
        General
        Video Games
    """)
    pick = input("Answer: ").upper().strip()
    if pick == "HISTORY":
        return 1
    elif pick == "MATH":
        return 2
    elif pick == "ANIMALS":
        return 3
    elif pick == "GENERAL":
        return 4
    elif pick[0:5]== "VIDEO":
        return 5
    else:
       print("That is not a category")
       print("Please choose a category")



def history_questions():

    loop = True
    while loop:
        with open("history","r") as infile:
            lines = infile.read().split()

        gen = random.choice(lines)

        if gen == "one":
            loop = False
            with open("history", "r") as r:
                strg = r.read()
            strg = strg.replace("one", "E")
            with open("history", "w") as w:
                w.write(strg)
            print()
            print("What year did World War 1 end?")
            ans = input("Answer: ")
            if ans == "1918":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "two":
            loop = False
            with open("history", "r") as r:
                strg = r.read()
            strg = strg.replace("two", "E")
            with open("history", "w") as w:
                w.write(strg)
            print()
            print("What year was the Declaration of Independence signed?")
            ans = input("Answer: ")
            if ans == "1776":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "three":
            loop = False
            with open("history", "r") as r:
                strg = r.read()
            strg = strg.replace("three", "E")
            with open("history", "w") as w:
                w.write(strg)
            print()
            print("In a 1752 experiment, a man proved lighting was electrical. Whom am I referring to?")
            ans = input("Answer: ").upper().strip()
            if ans[0:3] == "BEN":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "four":
            loop = False
            with open("history","r") as r:
                strg = r.read()
            strg = strg.replace("four","E")
            with open("history","w") as w:
                w.write(strg)
            print()
            print("The Silk Road were trade routes all throughout eurasia, documented for spreading goods, diseases and _ ? ")
            ans = input("Answer: ").upper().strip()
            if ans== "RELIGION":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"

        if all(x == "E" for x in lines[:4]):
            loop = False
            return "S"

def math_questions():

    loop = True
    while loop:
        with open("math","r") as infile:
            lines = infile.read().split()

        gen = random.choice(lines)

        if gen == "one":
            loop = False
            with open("math", "r") as r:
                strg = r.read()
            strg = strg.replace("one", "E")
            with open("math", "w") as w:
                w.write(strg)
            print()
            print("What is -7+4-5*6/2")
            ans = input("Answer: ")
            if ans == "-18":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "two":
            loop = False
            with open("math", "r") as r:
                strg = r.read()
            strg = strg.replace("two", "E")
            with open("math", "w") as w:
                w.write(strg)
            print()
            print("Finish the pattern 16 9 4 _")
            ans = input("Answer: ")
            if ans == "1":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "three":
            loop = False
            with open("math", "r") as r:
                strg = r.read()
            strg = strg.replace("three", "E")
            with open("math", "w") as w:
                w.write(strg)
            print()
            print("What is the cubed root of 343?")
            ans = input("Answer: ")
            if ans == "7":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "four":
            loop = False
            with open("math","r") as r:
                strg = r.read()
            strg = strg.replace("four","E")
            with open("math","w") as w:
                w.write(strg)
            print()
            print("What is 3√4-2? ")
            ans = input("Answer: ")
            if ans == "4":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"

        if all(x == "E" for x in lines[:4]):
            loop = False
            return "S"


def anim_questions():

    loop = True
    while loop:
        with open("animals","r") as infile:
            lines = infile.read().split()

        gen = random.choice(lines)

        if gen == "one":
            loop = False
            with open("animals", "r") as r:
                strg = r.read()
            strg = strg.replace("one", "E")
            with open("animals", "w") as w:
                w.write(strg)
            print()
            print("The fastest known aquatic animal with a burst top speed of 68 mph is the _")
            ans = input("Answer: ").upper().strip()
            if ans == "SAILFISH":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "two":
            loop = False
            with open("animals", "r") as r:
                strg = r.read()
            strg = strg.replace("two", "E")
            with open("animals", "w") as w:
                w.write(strg)
            print()
            print("Bats, dolphins, and shrews are all capable of using _")
            ans = input("Answer: ").upper().strip()
            if ans[0:4] == "ECHO":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "three":
            loop = False
            with open("animals", "r") as r:
                strg = r.read()
            strg = strg.replace("three", "E")
            with open("animals", "w") as w:
                w.write(strg)
            print()
            print("The oldest living animal is the _ which are estimated to live up to 10,000 to 15,000 years.")
            ans = input("Answer: ").upper().strip()
            if ans[0:3] == "GLA":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "four":
            loop = False
            with open("animals","r") as r:
                strg = r.read()
            strg = strg.replace("four","E")
            with open("animals","w") as w:
                w.write(strg)
            print()
            print("""
            What animal is this?
             
               ___---- _  -*-_
             /             ˆ  _}
             | /  ____--[  ]
             |_#          |_#
            
                  """)
            ans = input("Answer: ").upper().strip()
            if ans == "BEAR":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"

        if all(x == "E" for x in lines[:4]):
            loop = False
            return "S"



def video_questions():

    loop = True
    while loop:
        with open("video","r") as infile:
            lines = infile.read().split()

        gen = random.choice(lines)

        if gen == "one":
            loop = False
            with open("video", "r") as r:
                strg = r.read()
            strg = strg.replace("one", "E")
            with open("video", "w") as w:
                w.write(strg)
            print()
            print("How many mandatory bosses are in Terraria? Counting Lunar Pillars as one. ")
            ans = input("Answer: ")
            if ans == "10":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "two":
            loop = False
            with open("video", "r") as r:
                strg = r.read()
            strg = strg.replace("two", "E")
            with open("video", "w") as w:
                w.write(strg)
            print()
            print("The protagonist of GTAIV is _")
            ans = input("Answer: ").upper().strip()
            if ans[0:4] == "NIKO":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "three":
            loop = False
            with open("video", "r") as r:
                strg = r.read()
            strg = strg.replace("three", "E")
            with open("video", "w") as w:
                w.write(strg)
            print()
            print("A stack in MINECRAFT is _")
            ans = input("Answer: ")
            if ans == "64":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "four":
            loop = False
            with open("video","r") as r:
                strg = r.read()
            strg = strg.replace("four","E")
            with open("video","w") as w:
                w.write(strg)
            print()
            print("In Wii sports there are 5 sports, bowling, golf, boxing, baseball, and _ ")
            ans = input("Answer: ").upper().strip()
            if ans == "TENNIS":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"

        if all(x == "E" for x in lines[:4]):
            loop = False
            return "S"



def general_questions():

    loop = True
    while loop:
        with open("general","r") as infile:
            lines = infile.read().split()

        gen = random.choice(lines)

        if gen == "one":
            loop = False
            with open("general", "r") as r:
                strg = r.read()
            strg = strg.replace("one", "E")
            with open("general", "w") as w:
                w.write(strg)
            print()
            print("How many milliliters are in a liter? ")
            ans = input("Answer: ")
            if ans == "1000":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "two":
            loop = False
            with open("general", "r") as r:
                strg = r.read()
            strg = strg.replace("two", "E")
            with open("general", "w") as w:
                w.write(strg)
            print()
            print("An economic _ refers to when prices far exceed their real value, causing markets to crash")
            ans = input("Answer: ").upper().strip()
            if ans == "BUBBLE":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "three":
            loop = False
            with open("general", "r") as r:
                strg = r.read()
            strg = strg.replace("three", "E")
            with open("general", "w") as w:
                w.write(strg)
            print()
            print("Earths history is divided in to 4 major eras, precambrian, paleozoic, _, and cenozoic")
            ans = input("Answer: ").upper().strip()
            if ans == "MESOZOIC":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"
        elif gen == "four":
            loop = False
            with open("general","r") as r:
                strg = r.read()
            strg = strg.replace("four","E")
            with open("general","w") as w:
                w.write(strg)
            print()
            print("Dogs, bears, raccoons, and badgers belong to the suborder of Carnivora called _")
            ans = input("Answer: ").upper().strip()
            if ans == "CANIFORMIA":

                print("CORRECT")
                return "T"
            else:

                print("INCORRECT")
                return "F"

        if all(x == "E" for x in lines[:4]):
            loop = False
            return "S"

def play_again():

    again = input("Would you like to play again? : ")
    again.lower()

    if again[0] == "y" or again[0] == "s":
         return True
    else:
        return False

def reset():
    with open("history", "w") as w:
        w.write("""one
two
three
four""")
    with open("math", "w") as w:
        w.write("""one
two
three
four""")
    with open("animals", "w") as w:
        w.write("""one
two
three
four""")
    with open("video", "w") as w:
        w.write("""one
two
three
four""")
    with open("general", "w") as w:
        w.write("""one
two
three
four""")

def roll():
    die1= random.randint(1,6)
    die2 = random.randint(1,6)
    print(f"You rolled a {die1} and a {die2}.")
    sum = int(die1) + int(die2)
    return sum
