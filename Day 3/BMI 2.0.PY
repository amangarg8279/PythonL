height=float(input("please enter your height in m \n"))
weight=float(input("please enter your weight in kgs \n"))
bmi=round(weight/height**2)
print(bmi)
if bmi<18.5:
    print(f"your bmi is {bmi} , you are under weight .")
elif bmi >18.5 and bmi < 25:
    print(f"your bmi is {bmi} , you are in good shape .")
elif bmi >25 and bmi < 30:
    print(f"your bmi is {bmi} , you are slighty fat .")
elif bmi >30 and bmi < 35:
    print(f"your bmi is {bmi} , you have to start working out . ")
elif bmi >35:
    print(f"your bmi is {bmi} , Now your time is over go and hit the GYM . ")
