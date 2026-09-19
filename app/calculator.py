from app.operations import addition, subtraction, multiplication, division


def calculator():
    print("Simple Calculator")
    print("Enter operation and two numbers (e.g., add 2 3)")
    print("Type 'exit' to quit.")

    while True:
        user_input = input(">>> ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        parts = user_input.split()

        if len(parts) != 3:
            print("Invalid input. Please follow the format: operation number number")
            continue

        operation, num1, num2 = parts

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please follow the format: operation number number")
            continue

        if operation == "add":
            result = addition(num1, num2)

        elif operation == "subtract":
            result = subtraction(num1, num2)

        elif operation == "multiply":
            result = multiplication(num1, num2)

        elif operation == "divide":
            try:
                result = division(num1, num2)
            except ValueError as e:
                print(e)
                continue

        else:
            print(
                f"Unknown operation '{operation}'. "
                "Supported operations: add, subtract, multiply, divide."
            )
            continue

        print(f"Result: {result}")