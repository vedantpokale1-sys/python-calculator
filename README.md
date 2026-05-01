# python-calculator
A simple calculator built using Python that performs basic arithmetic operations like addition, subtraction, multiplication, and division.
# Python Calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting calculator...")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print("Invalid input! Please enter numbers.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", sub(num1, num2))

        elif choice == '3':
            print("Result:", mul(num1, num2))

        elif choice == '4':
            print("Result:", div(num1, num2))

    else:
        print("Invalid choice! Try again.")
