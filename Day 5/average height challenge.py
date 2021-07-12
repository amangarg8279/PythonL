#we will have average height of number of student and after that we have to calc the avearge height
total_of_height=0
height=[180,124,165,173,189,169,146]
for values in height:
    total_of_height+=values

print("Average height will  "+str(round(total_of_height/len(height),2))+" cm !")