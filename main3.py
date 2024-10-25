balance = int(input("Input account balance: "))
withdraw_amount = int(input("Input withdraw number: "))
if withdraw_amount > balance:
    print("Error: Not enough balance to withdraw said amount.")
else:
    balance -= withdraw_amount
    print("Remaining balance:", balance)
    if balance > 1000:
        print("Thank you for choosing BathSpa Bank.")
    elif balance < 100:
        print("Low-balance warning.")
    else:
        print("Good bye.")
        