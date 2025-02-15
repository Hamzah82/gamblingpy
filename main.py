import random
bal = 100
win = 0
lose = 0
def roll():
    global dice
    dice = random.randint(1,6)
print("Gambling simulation")
while bal > 0:
    print(" ")
    bet = int(input("How many balance you want to bet? "))
    print(" ")
    if bet > bal:
        print("Youre balance is under", bet)
    else:
        oddEven = int(input("Bet for? (odd = 1 even = 0) "))
        roll()
        print("The dice shown a", dice)
        if oddEven == 1:
            if dice % 2 == 0:
                print("You won!!")
                bal = bal + bet
                win = win + 1
            else:
                print("You loose")
                bal = bal - bet
                lose = lose + 1
        elif oddEven == 0:
            if dice % 2 == 0:
                print("You loose")
                bal = bal - bet
                lose = lose + 1
            else:
                print("You won!!")
                bal = bal + bet
                win = win + 1
    print(" ")
    print("You now have", bal, "balance")
    stop = input("Stop? (y/n) ")
    if stop == "y":
        break
i = 0
while i < 30:
    i = i + 1
    print(" ")

print("Your gambling stats")
print("Balance:", bal)
print("Win:", win)
print("Loose:", lose)
totalGame = win + lose
WR = win / totalGame * 100
print(f"Winrate: {WR}%")
profit = bal - 100
print("profit:", profit)