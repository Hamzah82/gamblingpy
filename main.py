import random
import time
import os

LEADERBOARD_FILE = "leaderboard.txt"

balance = 100  
wins = 0
losses = 0
streak = 0  
max_streak = 0  
level = 1   
xp = 0      
total_bet = 0  
games_played = 0  
biggest_win = 0  

def roll():
    return random.randint(1, 6)

def show_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        print("\n📜 The leaderboard is empty!")
        return
    
    print("\n🏆===== LEADERBOARD =====🏆")
    with open(LEADERBOARD_FILE, "r") as file:
        scores = [line.strip().split(",") for line in file.readlines()]
        scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[:5]  # Top 5
    
    for idx, (name, score) in enumerate(scores, start=1):
        print(f"{idx}. {name} - 💰 {score}")
    print("=========================")

def save_to_leaderboard(name, score):
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{name},{score}\n")

while True:
    print("\n🎲===== ULTIMATE GAMBLING SIMULATION =====🎲")
    choice = input("1️⃣ Play Game\n2️⃣ View Leaderboard\nChoose (1/2): ").strip()
    if choice == "2":
        show_leaderboard()
    elif choice == "1":
        break
    else:
        print("❌ Invalid choice!")

while balance > 0:
    print(f"\n💰 Balance: {balance} | 🏆 Level: {level} | ⭐ XP: {xp} | 🔥 Streak: {streak}")

    mode = "1"
    if level >= 10:
        mode = input("Select mode: 🎲 1 Dice (1) | 🎲🎲 2 Dice (2): ").strip()

    while True:
        try:
            bet = int(input("Enter your bet amount: "))
            if bet > balance:
                print("❌ Insufficient balance!")
            elif bet <= 0:
                print("❌ Bet must be more than 0!")
            else:
                break
        except ValueError:
            print("❌ Invalid input!")

    total_bet += bet
    games_played += 1  

    if mode == "1":
        odd_even = int(input("Bet on? (Odd = 1, Even = 0): "))
        
        dice = roll()
        print(f"🎲 The dice shows {dice}!")

        if (dice % 2 == 1 and odd_even == 1) or (dice % 2 == 0 and odd_even == 0):
            streak += 1
            xp += bet // 2  
            balance += bet
            wins += 1
            biggest_win = max(biggest_win, bet)
            print(f"✅ You WON! (+{bet})")
        else:
            print("❌ You LOST!")
            balance -= bet
            losses += 1
            streak = 0  

    elif mode == "2" and level >= 10:
        bet_type = int(input("Bet type: Odd/Even (1) | <7/>7 (2) | Exact Number (3) | Double (4): "))

        if bet_type == 1:
            odd_even = int(input("Bet on? (Odd = 1, Even = 0): "))

        elif bet_type == 2:
            range_bet = int(input("Bet: <7 (1) | >7 (2): "))

        elif bet_type == 3:
            number_guess = int(input("Guess the total dice value (2-12): "))

        elif bet_type == 4:
            print("Bet: You win if both dice show the same number (double).")

        dice1, dice2 = roll(), roll()
        total_dice = dice1 + dice2
        print(f"🎲🎲 The dice show {dice1} and {dice2}! (Total: {total_dice})")

        if bet_type == 1:
            if (total_dice % 2 == 1 and odd_even == 1) or (total_dice % 2 == 0 and odd_even == 0):
                streak += 1
                xp += bet // 2  
                balance += bet
                wins += 1
                biggest_win = max(biggest_win, bet)
                print(f"✅ You WON! (+{bet})")
            else:
                print("❌ You LOST!")
                balance -= bet
                losses += 1
                streak = 0  

        elif bet_type == 2:
            if (range_bet == 1 and total_dice < 7) or (range_bet == 2 and total_dice > 7):
                streak += 1
                xp += bet // 2  
                balance += bet
                wins += 1
                biggest_win = max(biggest_win, bet)
                print(f"✅ You WON! (+{bet})")
            else:
                print("❌ You LOST!")
                balance -= bet
                losses += 1
                streak = 0  

        elif bet_type == 3:
            if total_dice == number_guess:
                payout = bet * 5
                balance += payout
                wins += 1
                xp += payout // 5
                biggest_win = max(biggest_win, payout)
                print(f"🎯 JACKPOT! You won {payout}!")
            else:
                print("❌ You LOST!")
                balance -= bet
                losses += 1
                streak = 0  

        elif bet_type == 4:
            if dice1 == dice2:
                payout = bet * 3
                balance += payout
                wins += 1
                xp += payout // 5
                biggest_win = max(biggest_win, payout)
                print(f"🎯 DOUBLE! You won {payout}!")
            else:
                print("❌ You LOST!")
                balance -= bet
                losses += 1
                streak = 0  

    max_streak = max(max_streak, streak)

    if xp >= 100:
        level += 1
        xp -= 100  
        print(f"🎉 LEVEL UP! You are now Level {level}!")

    print(f"💰 Current balance: {balance}")

    if balance <= 0:
        print("\n💀 You ran out of money! Game Over.")
        break

    stop = input("Stop playing? (y/n): ").strip().lower()
    if stop == "y":
        break

player_name = input("\nEnter your name for the leaderboard: ").strip()
save_to_leaderboard(player_name, balance)

print("\n🎉 Thanks for playing! 🎉")
