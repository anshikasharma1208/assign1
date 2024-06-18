#Write a program that copies the contents of one text file to another
file1=open(r"C:/Users/sharm/OneDrive/Desktop/Assignment1/file1.txt",'r')
file2=open(r"C:/Users/sharm/OneDrive/Desktop/Assignment1/file2.txt",'w')
content=file1.read()
file2.write(content)
print("CONTENT COPIED!")