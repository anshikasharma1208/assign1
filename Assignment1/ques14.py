#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines=[]
while True:
    line = input("Enter a line :")
    if (line==''):
        break
    else:
        lines.append(line)
print(lines)


