height=int(input("please enter your height in cm "))
age=int(input("please enter your age "))
if height >=120:
    if age<=18:
        print("You have to pay $7")
    else:
        print("Sorry ! you are over 18 , you have to pay $12")
    print("Huraah ! lets go B-) ")
else:
    print("Sorry you are not elgibile for it  :-(")