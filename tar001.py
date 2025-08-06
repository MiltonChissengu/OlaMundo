# Basic Calculator Program
num1 = int(input("Type the first number: "))
num2 = int(input("Type the last number: "))
operator = input("Type the mathematical operation to result in these numbers: ")
if operator == '+':
    result = num1 + num2;
    print(num1," + ",num2," = ", result)
elif operator == '-':
    result = num1 - num2;
    print(num1," - ",num2," = ", result)
elif operator == '*':
    result = num1 * num2;
    print(num1," x ",num2," = ", result)
else:
    result = num1 / num2;
    print(num1," / ",num2," = ", result)