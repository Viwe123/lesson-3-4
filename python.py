# Question 1: Arithmetic and Assignment Operators
x = 11
y = 18
# TODO: Add 3 to x using the += operator
x += 3
# TODO: Multiply y by 2 using the *= operator
y *=2
# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a = 5
b = 8
c = 10

# TODO: Create a condition that checks if a is greater than b
condition1 = a > b
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
condition2 = b % 2 ==0
# TODO: Create a condition that checks if c is less than or equal to a
condition3 = c <=a
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = condition1 or (condition2 and condition3)
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
score = float(input("Enter a test score (0–100): "))

if 90 <= score <= 100:
    print("You got an A")
elif 80 <= score < 90:
    print("You got a B")
elif 70 <= score < 80:
    print("You got a C")
elif 60 <= score < 70:
    print("You got a D")
elif 0 <= score < 60:
    print("You got an F")
else:
    print("Please enter a score from 0 to 100.")

# TODO: Print the grade for the given score

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation (+, -, *, /): ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: cannot divide by zero"
else:
    result = "Error: invalid operation"

print("Result:", result)
# TODO: Handle the case of division by zero
if operation == "/":
    if num2 == 0:
        print("Error: cannot divide by zero.")
    else:
        print("Result:", num1 / num2)

# TODO: Print the result of the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error: cannot divide by zero."
    else:
        result = num1 / num2
else:
    result = "Error: invalid operation."

print("Result:", result)