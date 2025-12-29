def add(a, b):
    # BUG 1: returns subtraction instead of addition
    return a - b


def subtract(a, b):
    # BUG 2: wrong operator
    return a + b


def multiply(a, b):
    # BUG 3: returns string instead of number
    return str(a * b)


def divide(a, b):
    # BUG 4: no zero-division handling
    return a / b


def calculate(operation, x, y):
    # BUG 5: incorrect function mapping
    if operation == "add":
        return subtract(x, y)
    elif operation == "subtract":
        return add(x, y)
    elif operation == "multiply":
        return divide(x, y)
    elif operation == "divide":
        return multiply(x, y)
    else:
        raise ValueError("Unsupported operation")


def main():
    print("Calculator started")

    # BUG 6: inputs are strings, never converted
    x = input("Enter first number: ")
    y = input("Enter second number: ")

    # BUG 7: no input validation
    operation = input("Choose operation (add, subtract, multiply, divide): ")

    result = calculate(operation, x, y)

    # BUG 8: crash if result is string + number
    print("Result:", result + 1)


if __name__ == "__main__":
    main()
