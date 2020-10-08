# Snake Water Gun Game
# Man Vs Computer
# Used Random

import random
import time

ls = ["Snake", "Water", "Gun"]
pw = 0
cw = 0

print("\n\n\n\t\t\t\t**** SNAKE WATER GUN GAME ****\n")
time.sleep(2.5)

print("Instructions:")
time.sleep(0.6)
print("\n1. Input either 'Snake', 'Water or 'Gun'.")
time.sleep(1.7)
print("2. You will have to play 10 games against the computer")
time.sleep(1.9)
print("3. Whoever wins most games out of 10 is the final winner!!\n\n")
time.sleep(2.2)
print("Start By Entering your name below")
time.sleep(1)
pn = input("Enter your name: ")
ct = 1
time.sleep(1)
print(f"\nHi {pn}!\nGame starts!")
time.sleep(1)
while ct <= 10:
    p = input(f"\n\nRound {ct}\nEnter your choice[Snake/Water/Gun]: \n")
    c = random.randint(0, 2)
    time.sleep(1)
    cm = ls[c]
    if p == cm:
        print("\nTie!")
        ct += 1

    elif p == "Snake":
        if c ==1:
            print(f"\nThe snake drank all the water!!! {pn} wins round {ct}!!\n")
            ct += 1
            pw += 1
        else:
            print(f"\nThe snake was shot by the gun!!! Computer wins round {ct}!!\n")
            ct += 1
            cw +=1

    elif p == "Water":
        if c == 0:
            print(f"\nThe snake drunk all the water!!! Computer wins round {ct}!!\n")
            ct += 1
            cw += 1
        else:
            print(f"\nThe gun drowned in water!!! {pn} wins round {ct}!!\n")
            ct += 1
            pw += 1

    elif p == "Gun":
        if c == 0:
            print(f"\nThe snake was shot by the gun!!! {pn} wins round {ct}!!\n")
            ct += 1
            pw += 1

        else:
            print(f"\nThe gun drowned in water!!! Computer wins round {ct}!!\n")
            ct += 1
            cw += 1

    else:
        print("\nInput Error!!\n")

time.sleep(2)
print("\n\n10 Rounds Over!!!!")
time.sleep(1)
print(f"\nScore:\n\t Computer Wins: {cw}\n\t {pn} Wins: {pw}\n\t Ties: {10-pw-cw}\n\n")
time.sleep(3)
if pw > cw:
    print(f"************* {pn} Wins *************")
elif pw == cw:
    print("************* Game Tied *************")
else:
    print("************* Computer Wins *************")

