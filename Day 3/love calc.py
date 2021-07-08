name_first=input("Please enter your name \n")
name_sec =input("Please enter their name \n")

com_string=(name_first+name_sec).lower()
t=com_string.count("t")
r=com_string.count("r")
u=com_string.count("u")
e=com_string.count("e")
true=t+r+u+e

l=com_string.count("l")
o=com_string.count("o")
v=com_string.count("v")
e=com_string.count("e")
love=l+o+v+e

print(str(true)+str(love)+"%" )