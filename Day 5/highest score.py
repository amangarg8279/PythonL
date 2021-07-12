#we have to desgin a program so that we could get highest number in a class
numbers=[21,34,56,78,98,201,38,323,21,45]
highest_number=0
for value in numbers:
    if(highest_number<value):
        highest_number=value
print(highest_number)
print(max(numbers))
print(min(numbers))