def calculator():
    try_again = ""
    while try_again.lower() != "n":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operator = input("Enter operation(Add, Subtract, Multiply, Divide): ")
        if operator.lower() == "add":
            result = num1 + num2
        elif operator.lower() == "subtract":
            result = num1 - num2
        elif operator.lower() == "multiply":
            result = num1 * num2
        elif operator.lower() == "divide":
            result = num1 / num2
        else:
            print("Invalid input. Try again.")

        print(f"Result: {result}")

        try_again = input("Try again?: ")

calculator()