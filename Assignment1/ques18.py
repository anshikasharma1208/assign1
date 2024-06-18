#Write a python program that checks if two strings are anagrams of each other
str1=input("Enter a string : ")
str2=input("Enter another string : ")
if sorted(str1)==sorted(str2):
    print("Anagrams")
else:
    print("Not an anagram")
