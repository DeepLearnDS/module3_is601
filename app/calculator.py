from app.operations import addition, subtraction, multiplication, division


def calculator():
    print("Simple Calculator")
    print("Enter operation and two numbers (e.g., add 2 3)")
    print("Type 'exit' to quit.")

    while True:
        user_input = input(">>> ")

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        try:
            # Now we split the input into three parts: the operation (add, subtract, etc.) and the two numbers.
            operation, num1, num2 = user_input.split()
            # We have to make sure the numbers are actually numbers, so we convert them to floats.
            num1, num2 = float(num1), float(num2)
        except ValueError:
            # If the user doesn't type something correctly, like typing letters where numbers should be, we show an error.
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue  # This "continue" means: try again by going back to the top of the loop.

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