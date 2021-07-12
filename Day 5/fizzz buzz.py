#here we will write a program when a number is deviislbe by 3 it should print fizz . when a number divisble by
# 5 it should print buzz and when divisble by both then print fizz buzz

for var in range(1,101):
    if(var%3==0 and var%5==0):
        print("Fizz Buzz")
    elif(var%5==0):
        print("Buzz")
    elif(var%3==0):
        print("fizz")
    else:
        print(var)