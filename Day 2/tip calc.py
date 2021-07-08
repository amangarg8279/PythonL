total_amount=float(input("Please enter total amount of your bill "))
percen=float(input("please enter the % you want "))
peps=int(input("Enter number of peploe to distrubb"))

percent=float(total_amount*percen/100)
result=(percent+total_amount)/peps
print(round(result,2))
