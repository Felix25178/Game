from file import instructions, play_again, options,  history_questions, scores



def main():


    total = scores()
    on = True
    while on:
        instructions()
        while total < 100:

            print(f"Your score is: {total} ")
            option = options()
            if option == 1:
                history_questions()




        play= play_again()
        if play == False:
            print("Thank you for playing")
            on = False

if __name__ == '__main__':
    main()