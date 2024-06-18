#Write a python program that removes all punctuation from a given string
str1=input("Enter a string : ")
punctuation=".,;:!?"
for i in str1:
    if i in punctuation :
        str1=str1.replace(i,"")
print(str1)

