import random


def instructions():
    print("""
    _________________
    |Welcome to GAME|
    -----------------
    
    
    In this game you will choose a category and then answer a question in the category of your choosing.
    If you get it right you will be awarded points, get enough points and you win.
    
    Lets begin
    """)

def scores():
    score = 0
    return score

def add(score):
    int(score)
    score += 10
    return score

def subtract(score):
    int(score)
    score -= 10
    return score

def options():

    print(""" 
    ===================
    |CHOOSE A CATEGORY|
    -------------------
    
        History
        Math
        Animals
        Pop Culture
        Video Games
    """)
    pick = input("Answer: ").upper()
    if pick[0] == "H":
        return 1
    else:
       print("That is not a category")
       print("Please choose a category: ")





def history_questions():

    with open("history","r") as infile:
        lines = infile.read().split()
        lines = [int(x) for x in lines]
    gen = random.randint(lines[0], lines[3])

    if gen == 0:
        print()
        print("What year did World War 2 end?")
        ans = input("Answer: ")
        if ans == "1945":
            print("correct")

        else:
            print("Incorrect")
    elif gen == 1:
        print()
        print("quest2")
        ans = input("Answer: ")

        if ans == "2":
            print("correct")

        else:
            print("Incorrect")

    elif gen == 2:
        print()
        print("quest3")
        ans = input("Answer: ")

        if ans == "3":
            print("correct")

        else:
            print("Incorrect")
    elif gen == 3:
        print()
        print("quest4")
        ans = input("Answer: ")
        if ans == "4":
            print("correct")

        else:
            print("Incorrect")



def play_again():

    again = input("Would you like to play again? ")
    again.lower()

    if again[0] == "y" or again[0] == "s":
         return True
    else:
        return False