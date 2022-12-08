num1 = eval(input("Enter your first number:- "))
num2 = eval(input("Enter your Second number:- "))
op = input("Enter your operation (+,-,*,/):- ")

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Input. Enter a valid operation.")
