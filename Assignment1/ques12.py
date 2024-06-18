#Write a python program that calculates the sum of the digits of a given number
sum1 = 0
num = int(input("Enter the number"))
while (num != 0) :
    a = num % 10
    sum1 += a
    num = num//10
print("SUM IS:",sum1)


