# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
choice=input("Enter the sign ( + - * /) : ")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if choice=="+":
    res=num1+num2
    print("The sum of the given numbers: ",res)

elif choice=="-":
    if num1>num2:
        res=num1-num2
    else:
        res=num2-num1
    print("The difference of the given numbers: ",res)

elif choice=="*":
    res=num1*num2
    print("The multiplication of the given numbers: ",res)

elif choice=="/":
    if num1>num2:
        res=num1/num2
    else:
        res=num2/num1
    print("The division of the given numbers: ",res)
else:
    print("Invalid operator")