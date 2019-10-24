names = []
counter =0
while counter<10:
    name= input ("enter first name:")
    names.append(name)
    counter+=1
print (names)
end=False
while (end==False):
    print ("Enter a name to search for or 'End' to end the program:")
    search= input ("Enter a name you wish to search for:")
    if search == ("End"):
        print (" Game Over")
        end=True
    elif search in names:
         print("The name was found")
    elif search not in names:
         print(" The name was not found")


    
    
    
