'''
Author:Abisha Biju
program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
'''
temperature=int(input("enter the temperature:"))
unit=input("is this in (C)elsius or (F)ahrenheit:")
if unit=="C":
    f=(9/5*temperature)+32
    print(temperature, "celsius is",f,)
else:
    c = (5/9*temperature)-32
    print(temperature,"fahrenheit is",c,)

