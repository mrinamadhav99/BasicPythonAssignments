def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    return a ** b

def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a // b

# Dictionary of operators
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "//": floor_divide
}

def calculator():
    # First input
    num1 = int(input("Enter the first number: "))

    # Print available operators
    for operator in operations:
        print(operator)

    continue_flag = True

    while continue_flag:
        # User picks an operation
        op_symbol = input("Pick an operation from the list above: ").strip()

        if op_symbol not in operations:
            print("Invalid operation! Please select from the list.")
            continue

        # Second input
        num2 = int(input("Enter the second number: "))

        # Fetch the function based on the operator
        calculator_function = operations[op_symbol]

        # Calculate the result
        output = calculator_function(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {output}")

        # Ask if the user wants to continue
        should_continue = input(
            "Enter 'y' to continue calculation with the current result, 'n' to start a new calculation, or 'x' to exit: "
        ).lower()

        if should_continue == 'y':
            num1 = output
        elif should_continue == 'n':
            calculator()  # Start a new calculation
            return  
        elif should_continue == 'x':
            continue_flag = False
            print("Goodbye!")
        else:
            print("Invalid input. Exiting.")
            continue_flag = False

# Run the calculator
calculator()