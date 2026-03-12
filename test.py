import random

questions = [1, 2, 3, 4, 5, ]
gen = random.randint(questions[0], questions[5])
if gen == 0:
    ans = input("What year did World War 2 end?: ")
    if ans != "1945":
        print("Incorrect")
elif gen == 1:
    ans = input("plane strike?: ")
    if ans != "2001":
        print("Incorrect")
elif gen == 2:
    ans = input("plane strike?: ")
    if ans != "2002":
        print("Incorrect")
elif gen == 3:
    ans = input("plane strike?: ")
    if ans != "2003":
        print("Incorrect")
elif gen == 4:
    ans = input("plane strike?: ")
    if ans != "2004":
        print("Incorrect")
elif gen == 5:
    ans = input("Through out 1981 to 1986 : ").strip()
    if ans != "2005":
        print("Incorrect")