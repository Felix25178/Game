picked = False
while picked == False:

            print(""" 
            History
            Math
            Animals
            Pop Culture
            Video Games
                    """)
            pick = input("Choose a category: ").upper()

            if pick[0] == "H":
                picked = True

            else:
                print("That is not a category")
                print("Please choose a category: ")