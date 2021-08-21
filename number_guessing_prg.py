import random
winner_number = random.randint(1,100)
gues = 0
num = int(input("enter your number :-"))
cond = True
while True:
    if num == winner_number:
        print(f"you are win {gues} and this is your number {num} ")
        break
    else:
        if num > winner_number:
            print("too high")
            gues = gues + 1
            num = int(input("enter reagaing you number:-"))
        else:
            print("too low")
            gues = gues + 1
            num = int(input("enter your number"))
