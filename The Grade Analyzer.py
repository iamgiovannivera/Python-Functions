#3. The Grade Analyzer

# def main():
#     grades = []
#     print("Welcome to the Grade Analyzer!")

#     while True:
#         print("\nOptions:")
#         print("1. Add a grade")
#         print("2. Calculate average grade")
#         print("3. Find highest and lowest grade")
#         print("4. Categorize grades into letter grades")
#         print("5. Exit")

#         choice = input("Enter your choice (1/2/3/4/5): ")

#         if choice == '1':
#             grade = float(input("Enter the grade: "))
#             grades.append(grade)
#             print(f"Grade {grade} has been added.")
#         elif choice == '2':
#             average = calculate_average(grades)
#             print(f"The average grade is: {average}")
#         elif choice == '3':
#             highest, lowest = find_highest_and_lowest(grades)
#             print(f"The highest grade is: {highest}")
#             print(f"The lowest grade is: {lowest}")
#         elif choice == '4':
#             letter_grades = categorize_grades(grades)
#             print("Letter grades:")
#             for idx, letter in enumerate(letter_grades, 1):
#                 print(f"Grade {grades[idx-1]} is a {letter}")
#         elif choice == '5':
#             print("Thank you for using the Grade Analyzer! Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

# if __name__ == "__main__":
#     main()
