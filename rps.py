import random


while True:
   
    ch = random.randint(1,3)
    print("Select your choice:")
    
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    p1 = int(input("1,2 or 3:"))

    print(f"You have chosen {p1}")

    if p1 == ch:
        print("It's a Tie")
    else:
        if p1 == 1 :
            if ch == 3:
                print("You Win.Rock smashes Scissors") 
            else:
                print("You lose.Paper covers Rock")
        elif p1 == 2:
            if ch == 1:
                print("You Win.Paper covers Rock")
            else:
                print("You lose.Scissors cut Paper")
        else:
            if ch == 2:
                print("You win.Scissors cut Paper")
            else:
                print("You lose.Rock smashes Scissors")
    print("Try again?")
    try2 = input("y/n")
    if try2.lower() != "y":
        break