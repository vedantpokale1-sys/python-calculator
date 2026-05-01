# Number Utility Program using Functions

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def factorial(n):
    if n < 0:
        return "Not defined"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def check_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"


def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


while True:
    print("\n--- Number Utility Program ---")
    print("1. Check Even/Odd")
    print("2. Factorial")
    print("3. Check Prime")
    print("4. Sum of numbers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting...")
        break

    num = int(input("Enter a number: "))

    if choice == '1':
        print("Result:", check_even_odd(num))

    elif choice == '2':
        print("Factorial:", factorial(num))

    elif choice == '3':
        print("Result:", check_prime(num))

    elif choice == '4':
        print("Sum:", sum_numbers(num))

    else:
        print("Invalid choice!")
