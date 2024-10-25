'''
Author:Abisha Biju
program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
'''
number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
if(number1>0):
    print(number1,"is greater than",number2)
else:
    print(number2,"is greater than",number1)
    print("the remaining statements")