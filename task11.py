def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Error: Division by zero!" if b == 0 else a / b

def power(a, b):
    return a ** b

def floor_divide(a, b):
    return "Error: Division by zero!" if b == 0 else a // b

# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "//": floor_divide
}

def calculator():
    # Get initial number
    first_number = int(input("Enter the first number: "))

    # Display available operators
    print("Available operations:")
    for operator in operations.keys():
        print(operator)

    keep_calculating = True

    while keep_calculating:
        # Choose an operator
        operator = input("Choose an operation from the list above: ").strip()

        if operator not in operations:
            print("Invalid operation! Please choose a valid one.")
            continue

        # Get the second number
        second_number = int(input("Enter the second number: "))

        # Perform the calculation
        operation_function = operations[operator]
        result = operation_function(first_number, second_number)
        print(f"Result: {first_number} {operator} {second_number} = {result}")

        # Decide the next step
        next_step = input(
            "Enter 'y' to continue with the current result, 'n' for a new calculation, or 'x' to exit: "
        ).lower()

        if next_step == 'y':
            first_number = result
        elif next_step == 'n':
            calculator()  # Restart the calculator
            return
        elif next_step == 'x':
            keep_calculating = False
            print("Thank you for using the calculator. Goodbye!")
        else:
            print("Invalid input. Exiting.")
            keep_calculating = False

# Start the calculator
calculator()
