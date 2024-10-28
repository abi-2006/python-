balance_amount=1000
while True:
    print("1.\tcheck balance")
    print("2.\tdeposit money")
    print("3.\twithdraw money")
    print("4.\texit")
    choice=int(input("enter your choice:"))
    if choice == 1:
        print(f"the current balance ${balance_amount}")
    elif choice == 2:
        deposit_amount=float(input("enter the amount"))
        balance_amount=balance_amount +deposit_amount
        print(f"the deposited_amount ${deposit_amount} and"
              f"the current balance ${balance_amount}")
    elif choice == 3:
        withdraw_amount = float(input("enter the amount to withdraw:"))
        balance_amount = balance_amount-withdraw_amount
        print(f"the amount withdrawn from the account ${withdraw_amount} the balance amount ${balance_amount}")
        if balance_amount < withdraw_amount:
            print("insufficient amount")
    elif choice == 4:
        break
    else:
        print("invalid entry")

