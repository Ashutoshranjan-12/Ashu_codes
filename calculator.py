# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide the first number by the second
def divide(a, b):
    # Check for division by zero
    if b == 0:
        return "Error! Division by zero is not possible"
    else:
        return a / b

# Function to perform calculator operations
def calculator():
    # Display available operations
    print("Select operation to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for the operation choice
    choice = input("Enter the choice (1, 2, 3, 4):")

    # Check if the choice is valid
    if choice in ['1', '2', '3', '4']:
        # Get user input for the two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation and display the result
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        # Display error message for invalid input
        print("Invalid input!")

# Call the calculator function to run the program
calculator()