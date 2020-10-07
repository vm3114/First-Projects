

age = int(input("Enter your age: "))

if age<18:
    print("You are too small to start driving. Please wait for around", 18-age ,"years to start driving.")
elif age>18 and age<70:
    print("Feel free to drive!!!")
elif age>=70:
    print("You are adviced not to drive because you are too old.")
elif age == 18:
    print("We aren't sure if you can drive or not. Please get yourself tested!")
else:
    print("Enter an integer as your age please!")
