print("\n\t\t\t\t Welcome to Guess The Number Game.\n You need to enter a 2 digit number and if it's the lucky number, You win!")
print("\n \t\t\t\t\t RULES\n \t\t\t 1. You get only 5 tries. \n \t\t\t 2. Enter Only a 2 Digit Number!\n\n")


n = 23
i = 0
while True:
    if i ==10:
        print("Maximum 10 Tries Allowed!!!\n Game Over.")
        break
    g = int(input("Enter a number: "))
    if g == n:
        print("Good Guess! \n \t You Win!!!")
        break
    elif g < n:
        i = i + 1
        print("Enter a larger number. You have", 10-i , "tries remaining.")
        continue
    elif g > n:
        i = i + 1
        print("Enter a smaller number.  You have", 10-i , "tries remaining.")
        continue

    else:
        print("Recheck What You Put and restart the program")
