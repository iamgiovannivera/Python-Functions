# # Task 1


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error! Division by zero."
#     return a / b

# # Task 2
    
# def get_number(prompt):
#     while True:
#         try:
#             number = float(prompt)
#             return number
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def get_operation():
#     operations = ['+', '-', '*', '/']
#     while True:
#         operation = input("Enter an operation (+, -, *, /): ")
#         if operation in operations:
#             return operation
#         else:
#             print("Invalid operation. Please enter one of +, -, *, /.")

# def main():
#     print("Welcome to the Calculator App!")
#     while True:
#         num1 = get_number(input("Enter the first number: "))
#         num2 = get_number(input("Enter the second number: "))
#         operation = get_operation()

#         if operation == '+':
#             result = add(num1, num2)
#         elif operation == '-':
#             result = subtract(num1, num2)
#         elif operation == '*':
#             result = multiply(num1, num2)
#         elif operation == '/':
#             result = divide(num1, num2)

#         print(f"The result is: {result}")

#         another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
#         if another_calculation != 'yes':
#             print("Thank you for using the Calculator App!")
#             break

# if __name__ == "__main__":
#     main()
