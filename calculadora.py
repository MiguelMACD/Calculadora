
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    else:
        return num1 / num2

def validate_option(option):
    if option not in ['1', '2', '3', '4', '5']:
        return False
    return True

def calculator():
    while True:
        print("\nSelect the operation you want to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        option = input("\nEnter the number of the desired operation: ")

        if not validate_option(option):
            print("Invalid option. Please select a valid option.")
            continue

        if option == '5':
            print("Exiting the calculator")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if option == '1':
            print("The result of addition is:", addition(num1, num2))
        elif option == '2':
            print("The result of subtraction is:", subtraction(num1, num2))
        elif option == '3':
            print("The result of multiplication is:", multiplication(num1, num2))
        elif option == '4':
            print("The result of division is:", division(num1, num2))

calculator()