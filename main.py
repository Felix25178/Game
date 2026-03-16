###############################################
#
#  Code for CS 161P Final Exam
#
#  Task: Create a program
#  Author: Alexander Green
#  Date: 3/14/26
#
#  Filename: Final_Exam_alex_green
#
###############################################

from file import instructions, play_again, options,  history_questions, math_questions, reset, anim_questions, video_questions, general_questions, roll



def main():

    on = True
    while on:
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        points = 0
        reset()
        instructions()
        while -30 < points < 100:
            print()
            print(f"Your score is {points} ")
            option = options()
            if option == 1:
                question1 = history_questions()
                if question1 == "T":
                    points += 10
                if question1 == "F":
                    points -= 10
                if question1 == "S":
                    print("All questions have been answered")
                    print("SELECT A DIFFERENT CATEGORY")
                    option = options()
            elif option == 2:
                question2 = math_questions()
                if question2 == "T":
                    points += 10
                if question2 == "F":
                    points -= 10
                if question2 == "S":
                    print("All questions have been answered")
                    print("SELECT A DIFFERENT CATEGORY")
                    option = options()

            elif option == 3:
                question3 = anim_questions()
                if question3 == "T":
                    points += 10
                if question3 == "F":
                    points -= 10
                if question3 == "S":
                    print("All questions have been answered")
                    print("SELECT A DIFFERENT CATEGORY")
                    option = options()
            elif option == 4:
                question4 = general_questions()
                if question4 == "T":
                    points += 10
                if question4 == "F":
                    points -= 10
                if question4 == "S":
                    print("All questions have been answered")
                    print("SELECT A DIFFERENT CATEGORY")
                    option = options()
            elif option == 5:
                question5 = video_questions()
                if question5 == "T":
                    points += 10
                if question5 == "F":
                    points -= 10
                if question5 == "S":
                    print("All questions have been answered")
                    print("SELECT A DIFFERENT CATEGORY")
                    option = options()

            if (question5== "S") and (question4== "S") and (question3== "S") and (question2== "S") and (question1 == "S"):
                points = -30

            if points == 60:
                print("""
                
                   ******************
                 *    O   O      *  *
               *****************    *
               *   O           *  O *
               *       O       *    *
               *           O   *  *
               *****************
               
               #*≈≈≈≈≈≈≈≈≈≈≈≈*#
               | GAMBLE TIME! | 
               #*≈≈≈≈≈≈≈≈≈≈≈≈*#
                """)
                gamble = input("Would you like to roll 2 dice for a chance to gain double points?: ").upper()
                if gamble[0] == "Y":
                    print("""
                        
                    You will be given two die to roll, if the sum of the dice is higher than 7 you win.
                    Otherwise you will lose points.
                    To roll input "r".
                        
                    """)
                    rolling = input("Roll dice : ").lower()
                    while rolling != "r":
                        rolling = input("Roll dice : ")
                    if rolling == "r":
                        print("Rolling...")
                        rol=roll()
                        if rol > 7:
                            print("""                           
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    YOU WON 20 POINTS!
    ------------------
                            """)
                            points += 20
                        else:
                            print("""
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    YOU LOST 20 POINTS
    ------------------
                            """)
                            points -= 20
                if gamble[0] != "Y":
                    print("You declined to gamble.")


            if points == 100:
                print(F"""
                ____________________________
                  
                  *************************
                  CONGRATULATIONS! YOU WIN!
                  *************************
                      FINAL SCORE {points}
                ____________________________
                """)
                play = play_again()
                if play == False:
                    print("Thank you for playing")
                    on = False

            if points == -30:
                print(F"""
                ____________________
                ////////////////////
                GAME OVER...YOU LOSE
                ////////////////////
                  FINAL SCORE {points}
                --------------------
                """)
                play = play_again()
                if play == False:
                    print("Thank you for playing")
                    on = False


if __name__ == '__main__':
    main()
