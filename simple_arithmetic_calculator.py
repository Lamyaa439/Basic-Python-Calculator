print('Basic Calculator')

while True:
    operator= input("Enter an operator (+, -, *, /) or type Q or q to quit: ")

    if operator.lower()=='q':
        break

    if operator not in '+-*/':
        print("that is not a valid operator!")
        continue

    num1= float(input("Enter the first number:"))
    num2= float(input("Enter the second number:"))

    if operator == "+":
        result = num1 + num2
        print(num1, '+', num2, '=', result)
    elif operator == "-":
        result = num1 - num2
        print(num1, '-', num2, '=', result)
    elif operator == "*":
        result = num1 * num2
        print(num1, '*', num2, '=', result)
    elif operator == "/":
        if num2 ==0:
            print("You can not divide a number by Zero!")
        else:   
            result = num1 / num2
            print(num1, '/', num2, '=', round(result,3))
   

print("Goodbye")    
           