'''
Author:Abisha Biju
a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit
'''
while True:
    print("1.\ttemperature in celsius to fahrenheit")
    print("2.\ttemperature in fahrenheit to celsius")
    print("3.\texit the program")
    choice=int(input("enter your choice:"))
    if choice == 1:
        temperature=float(input("enter temperature in celsius:"))
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"temperature in fahrenheit {fahrenheit}")
    elif choice == 2:
        temperature=float(input("enter temperature in fahrenheit:"))
        celsius = (temperature - 32) * 5 / 9
        print(f"temperature in celsius {celsius}")
    elif choice == 3:
        exit()
    else:
        print("error")