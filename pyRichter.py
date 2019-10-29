#Python Richter Scale Calculation
#Your first and last name:
#Your ID:

#Algorithm:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)

# test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6

Richter= input ("Enter the Richter scale value:")
End=False
while (End==False):

    if float(Richter)>=8.0:
        print ("most structures fall:")
        End=True
    elif float(Richter)>=7.0:
        print ("Many buildings destroyed")
        End=True
    elif float(Richter)>=6.0:
        print:("Many buildings considerably damaged, some collapse")
        End=True
    elif float(Richter)>=4.5:
        print ("Damage to poorly constructed buildings")
        End=True
    elif float(Richter)<4.5:
        print(" No destruction of buildings")
        End=True
           
 
