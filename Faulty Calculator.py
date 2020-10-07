
# Faulty Calculator
# All operations done correctly except 45*3 (or 3*45) , 56+9 (or 9+56) and 56/9

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
op = input("Enter an operator [ +,-,*,/ ]: ")

if op=="+":


    if n1 == 56  and n2 == 9 :
        print("Your answer is: \n 77")
    elif n1 == 9 and n2 == 56 :
        print("Your answer is: \n 77")
    else:
        print("Your answer is: \n ",n1 + n2)


elif op=="-":
    print("Your answer is: \n ",n1-n2)


elif op=="*":
    if n1 == 45 and n2 == 3:
        print("Your answer is: \n 555")
    elif n1 == 3 and n2 == 45:
        print("Your answer is: \n 555")
    else:
        print("Your answer is: \n ",n1*n2)

elif op == "/":
    if n1 == 56 and n2 == 6 and op == "/":
        print("Your answer is: \n 4")
    else:
        print("Your answer is: \n ", n1 / n2)



else:
    print('ENTER A VALID NUMBER OR OPERARTOR!')