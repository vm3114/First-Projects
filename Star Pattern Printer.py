# Star Pattern Printer
# Can Print in increasing or decreasing order

print("\n\t\t\t\t\t *****STAR PATTERN PRINTER*****")
print("Enter the height of the pattern and then enter the order of stars for your pattern\n\n")
try :
    a = int(input("Enter the height: "))
    n = int(input("Enter 0 for stars in increasing order, 1 for decreasing: "))

except ValueError:
    print("\nEnter a number only!!")                                    

if n >1 or n<0:
    print("Enter only 0 or 1!")

else:
    g =0
    print("\n Here is your pattern:\n\n")
    if n == 0:
        while g <a:
            print("* "*g)
            g = g+1

    elif n==1:
        while g < a:
            print("* "* (a-g))
            g = g+1
