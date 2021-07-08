#in this challenge we are looking a member from gang to pay the bill
import random
#taking input from user
name=input("Please enter your names sperated by Comma(,) \n")
#converting data to list
names=name.split(",")
#checking length of it
names_len=len(names)
#appying random function to get random name
random_num=random.randint(0,names_len-1)
print(names[random_num])
#using random function for list
print(random.choice(names))
