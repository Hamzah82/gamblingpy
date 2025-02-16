import random
import time
import os

# File penyimpanan leaderboard
LEADERBOARD_FILE = "leaderboard.txt"

# Inisialisasi variabel
bal = 100  
win = 0
lose = 0
streak = 0  
max_streak = 0  
level = 1   
xp = 0      
jackpot_bonus = 50  
total_bet = 0  
games_played = 0  
biggest_win = 0  

# Fungsi untuk melempar dadu
def roll():
    return random.randint(1, 6)

# Fungsi menampilkan leaderboard
def show_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        print("\n📜 Leaderboard masih kosong!")
        return
    
    print("\n🏆===== LEADERBOARD =====🏆")
    with open(LEADERBOARD_FILE, "r") as file:
        scores = [line.strip().split(",") for line in file.readlines()]
        scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[:5]  # Top 5
    
    for idx, (name, score) in enumerate(scores, start=1):
        print(f"{idx}. {name} - 💰 {score}")
    print("=========================")

# Fungsi menyimpan skor ke leaderboard
def save_to_leaderboard(name, score):
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{name},{score}\n")

# Menu utama
while True:
    print("\n🎲===== ULTIMATE GAMBLING SIMULATION =====🎲")
    choice = input("1️⃣ Main Game\n2️⃣ Lihat Leaderboard\nPilih (1/2): ").strip()
    if choice == "2":
        show_leaderboard()
    elif choice == "1":
        break
    else:
        print("❌ Pilihan tidak valid!")

# Gameplay utama
while bal > 0:
    print(f"\n💰 Saldo: {bal} | 🏆 Level: {level} | ⭐ XP: {xp} | 🔥 Streak: {streak}")
    
    # Pemilihan mode
    mode = "1"
    if level >= 10:
        mode = input("Pilih mode: 🎲 1 Dadu (1) | 🎲🎲 2 Dadu (2): ").strip()

    # Input taruhan
    while True:
        try:
            bet = int(input("Masukkan jumlah taruhan: "))
            if bet > bal:
                print("❌ Saldo tidak cukup!")
            elif bet <= 0:
                print("❌ Taruhan harus lebih dari 0!")
            else:
                break
        except ValueError:
            print("❌ Input tidak valid!")

    total_bet += bet
    games_played += 1  

    if mode == "1":
        dice = roll()
        print(f"🎲 Dadu menunjukkan angka {dice}!")
        oddEven = int(input("Taruhannya? (Ganjil = 1, Genap = 0): "))

        if (dice % 2 == 1 and oddEven == 1) or (dice % 2 == 0 and oddEven == 0):
            streak += 1
            xp += bet // 2  
            bal += bet
            win += 1
            biggest_win = max(biggest_win, bet)
            print(f"✅ Anda MENANG! (+{bet})")
        else:
            print("❌ Anda KALAH!")
            bal -= bet
            lose += 1
            streak = 0  

    elif mode == "2" and level >= 10:
        dice1, dice2 = roll(), roll()
        total_dice = dice1 + dice2
        print(f"🎲🎲 Dadu menunjukkan {dice1} dan {dice2}! (Total: {total_dice})")
        bet_type = int(input("Taruhan: Ganjil/Genap (1) | <7/>7 (2) | Angka Spesifik (3) | Double (4): "))

        if bet_type == 1:
            oddEven = int(input("Taruhannya? (Ganjil = 1, Genap = 0): "))
            if (total_dice % 2 == 1 and oddEven == 1) or (total_dice % 2 == 0 and oddEven == 0):
                streak += 1
                xp += bet // 2  
                bal += bet
                win += 1
                biggest_win = max(biggest_win, bet)
                print(f"✅ Anda MENANG! (+{bet})")
            else:
                print("❌ Anda KALAH!")
                bal -= bet
                lose += 1
                streak = 0  

        elif bet_type == 2:
            range_bet = int(input("Taruhan: <7 (1) | >7 (2): "))
            if (range_bet == 1 and total_dice < 7) or (range_bet == 2 and total_dice > 7):
                streak += 1
                xp += bet // 2  
                bal += bet
                win += 1
                biggest_win = max(biggest_win, bet)
                print(f"✅ Anda MENANG! (+{bet})")
            else:
                print("❌ Anda KALAH!")
                bal -= bet
                lose += 1
                streak = 0  

        elif bet_type == 3:
            number_guess = int(input("Tebak total angka dadu (2-12): "))
            if total_dice == number_guess:
                payout = bet * 5
                bal += payout
                win += 1
                xp += payout // 5
                biggest_win = max(biggest_win, payout)
                print(f"🎯 Jackpot! Anda menang {payout}!")
            else:
                print("❌ Anda KALAH!")
                bal -= bet
                lose += 1
                streak = 0  

        elif bet_type == 4:
            if dice1 == dice2:
                payout = bet * 3
                bal += payout
                win += 1
                xp += payout // 5
                biggest_win = max(biggest_win, payout)
                print(f"🎯 Double! Anda menang {payout}!")
            else:
                print("❌ Anda KALAH!")
                bal -= bet
                lose += 1
                streak = 0  

    max_streak = max(max_streak, streak)

    if xp >= 100:
        level += 1
        xp -= 100  
        print(f"🎉 Level UP! Anda sekarang Level {level}!")

    print(f"💰 Saldo sekarang: {bal}")

    if bal <= 0:
        print("\n💀 Anda kehabisan saldo! Game Over.")
        break

    stop = input("Berhenti? (y/n): ").strip().lower()
    if stop == "y":
        break

# Pemain memasukkan nama untuk leaderboard
player_name = input("\nMasukkan nama Anda untuk leaderboard: ").strip()
save_to_leaderboard(player_name, bal)

# Statistik akhir
print("\n🎲===== STATISTIK AKHIR =====🎲")
print(f"💰 Saldo Akhir     : {bal}")
print(f"🏆 Level Akhir     : {level}")
print(f"✅ Menang          : {win}")
print(f"❌ Kalah          : {lose}")
print(f"🔥 Streak Tertinggi: {max_streak}")
print(f"💸 Kemenangan Terbesar: {biggest_win}")
print(f"📊 Rata-rata Taruhan: {total_bet / games_played:.2f}" if games_played > 0 else "📊 Rata-rata Taruhan: 0")

print("\n🎉 Terima kasih telah bermain! 🎉")
