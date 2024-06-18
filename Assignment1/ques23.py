#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
choice=input("Enter F to convert Fahrenheit to celsius and C to convert celsius to Fahrenheit : ")
temp=int(input("Enter the temperature: "))

if choice=="F":
    cel=(temp-32) /1.8
    print ("FAHRENHEIT : ",cel)

if choice=="C":
    fah=(temp*1.8) +32
    print("CELSIUS : ",fah)

