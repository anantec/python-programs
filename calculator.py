def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def sub(a,b):
    return a-b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def calculator():
    while True:
        a = int(input("Enter the first number: "))
        b = int(input("\nEnter the second number: "))

        print("\nEnter for Operations:")
        print("Enter 1 for addition")
        print("Enter 2 for multiplication")
        print("Enter 3 for subtraction")
        print("Enter 4 for division")
        print("Enter 5 to quit")

        choice = int(input("\nChoose the following option to perform the operation on the given numbers: "))

        if choice == 1:
            result = add(a, b)
            print("The addition is: ", result)
        elif choice == 2:
            result = mul(a, b)
            print("The multiplication is: ", result)
        elif choice == 3:
            result = sub(a, b)
            print("The substraction is: ", result)
        elif choice == 4:
            result = divide(a, b)
            print("The division is: ", result)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

calculator()

