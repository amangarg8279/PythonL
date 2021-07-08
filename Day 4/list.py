person1=["Aman Garg" , 21 , "TCS" ,"MCA"]
print(person1) #printing all the elements of list

print(person1[0]) #printing only first element of list

#changing the value of index 0

person1[0]="Aman"
print(person1[0])

#adding new value to the list

person1.append("CCSU")
print(person1)
print(person1[-1])

#add another list the pre existing list
person1.extend(["CCSU","Money"])
print(person1)