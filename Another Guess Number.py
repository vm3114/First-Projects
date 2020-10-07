print("\n\t\t\t\t Welcome to Guess The Number Game.\n You need to enter a 2 digit number and if it's the lucky number, You win!")
print("\n \t\t\t\t\t RULES\n \t\t\t 1. You get only 5 tries. \n \t\t\t 2. Enter Only a 2 Digit Number!\n\n")
n = ""
i = 1
while n != 23 and i<=5:
    n = int(input("Input a 2 digit number: "))
    if n!=23 and  i!=5 :
        print("\nWrong Guess, Enter Again! You Have", 5-i ,"trie(s) left!")
        i +=1
    else:
        i+=1
if i >5:
    print("\n\n\t\t5 Tries Over!!! You Lose! :(")
else:
    print("\n\n\t\tCorrect guess!!! You Win!!")