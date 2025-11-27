import  arithmetic_operations

arithmetic_operations.perfom_operation
print("Arithmetic Operations")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
if operation == "add":
    result = num1 + num2
elif operation  == "substract":
    result =  num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 == 0:
        print("Error:can't divide by zero !")
    result = num1 / num2
else:
    print("Error invalid operator")
print(f"Result: {result}")
