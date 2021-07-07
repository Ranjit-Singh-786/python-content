winnernum = 43
gues = 1
game_over = False
numb =int(input("enter number between 1 to 100  "))
while not game_over:
    if winnernum == numb:
        print(f"you win, and your guess num {gues}")
        game_over = True
    else:
        if winnernum < numb:
            print("too high !")
            gues = gues + 1
            numb =int(input("enter again number  "))
        else:
            print("too low !")
            gues = gues + 1
            numb = int(input("please retry and enter again your number : "))