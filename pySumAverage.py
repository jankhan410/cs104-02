numberList=[ ]
total=0
for x in range(0,20):
    number=float(input("Enter in A Number:"))
    numberList.append(number)
    total=total+number


average=total/len(numberList)

total=str(total)
average=str(average)
print ("The Sum of The List is " +total)
print("The Average of the list is "+ average)
print("Thanks For Running My Program!")






