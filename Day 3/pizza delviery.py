#pizza charges
size=input("Please enter the size of pizza  ? S / M / L  ? ")
pepp=input("You want peppronie on it ? Y / N ")
extra_cheese=input("You want Extra cheese on it ? Y / N ")
total_bill=0
if size== "S" :
    total_bill+=15
if size== "M" :
    total_bill+=20
if size== "L" :
    total_bill+=25
if pepp=="Y":
    if size=="S":
        total_bill+=2
    else:
        total_bill+=3
if extra_cheese=="Y":
    total_bill+=1

print(f"Your total bill is for {total_bill} of size {size} :) ")