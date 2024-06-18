#Write a python program that returns the minimum and maximum values in a list of numbers
n=5
list1=[]
for i in range(5):
    num=int(input("Enter the elements:"))
    list1.append(num)
maxx=0
mini=list1[0]
print("The list : ",list1)
for i in list1:
    if maxx<i:
        maxx=i
for i in list1:
    if mini>i:
        mini=i
print("Maximum number : ", maxx)
print("Minimum number : ",mini)
