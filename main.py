total_bill = float(input("Input total bill: "))
if total_bill >= 50:
    total_bill *= .9
    print("Discount:", total_bill,"£")
else:
    print("No Discount:", total_bill,"£")