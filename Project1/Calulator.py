#print the menu
print("What operation would you like to perform?")
print("1) Addition")
print("2) Subtraction")
print("3) Division")
print("4) multiplication")
print("5) Modulus")

#take input from the user for their choice
selection = int(input(""))

#use if statements to tell the user what operation they selected
if selection == 1:
    print("Addition was selected")
elif selection == 2:
    print("Subtraction was selected")
elif selection == 3:
    print("Division was selected")
elif selection == 3:
    print("Multiplication was selected")
elif selection == 4:
    print("Modulus was selected")

#take input from user for the interes to calculate, save them to variables
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))

#use if statements to do the requested calculation and output the answer to the user
if selection == 1:
    answer = int1 + int2
    print("The sum of " +str(int1)+ " and " +str(int2) + " is: " + str(answer))
elif selection == 2:
    answer = int1 - int2
    print("The difference of " + str(int1) + " and " + str(int2) + " is: " + str(answer))
elif selection == 3 and int2 != 0:
    answer = int1 / int2
    print("The quotient of " + str(int1) + " and " + str(int2) + " is: " + str(answer))
elif selection == 3 and int2 == 0:
    print("You cannot divide by 0")
elif selection == 4:
    answer = int1 * int2
    print("The product of " + str(int1) + " and " + str(int2) + " is: " + str(answer))
elif selection == 5 and int2 != 0:
    answer = int1 % int2
    print("The modulus of " + str(int1) + " and " + str(int2) + " is: " + str(answer))
elif selection == 5 and int2 == 0:   
    print("You cannot divide by 0")








