def perfom_operation(num1,num2,operation):
    operation = operation.lower().strip()

    if operation == "add":
        result == num1 + num2
    elif operation  == "substract":
        result ==  num1 - num2
    elif operation == "multiply":
        result == num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error:can't divide by zero !"
        result == num1 / num2
    else: 
        return "Error invalid operator"
