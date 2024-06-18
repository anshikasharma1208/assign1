#Write a python program that takes a list of numbers and returns their sum
n=int(input("Enter the number of numbers to add: "))
sum1=0
list1=[]
for i in range (n):
    num=int(input("Enter the number:"))
    list1.append(num)
print("The list :",list1)
for i in list1:
    sum1+=i
print("The sum of numbers :",sum1)