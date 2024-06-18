#Write a python program that counts the occurrences of a specific element in a list
list1 = ['h','u','1',"2",'o',"2",'r',"2",'u']
element = input("Enter the specific element to count the occurrence: ")
count=0
for i in list1:
    if i==element:
        count += 1
print ("Count of the element",count)
