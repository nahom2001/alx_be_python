





def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide": 
        if num2 == 0:
            return "Zero division is not allowed"
        else: 
            result = num1 / num2

    return result

