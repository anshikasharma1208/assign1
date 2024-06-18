# Write a program in python that counts the frequency of each character in a string
str1=input("Enter a string: ")
str2=input ("Enter the character to search: ")
count=0
for i in str1:
    if (i==str2):
        count+=1
print(count)