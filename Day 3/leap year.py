year =int(input("Enter any year ! \n"))
if year%4==0:
    if year %100==0:
        if year % 400 ==0:
            print("Congrats its an leap year :->")
        else:
            print(" this year is not a leap year :-<")
    else:
            print(" this year is not a leap year :-<")
else:
            print(" this year is not a leap year :-<")
