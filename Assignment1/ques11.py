num=int(input("Enter the number of Fibonacci numbers to generate: "))
count=0
n1,n2=0,1
if num <= 0:
    print("Incorrect input")
elif num == 1:
    print("Fibonacci sequence upto",num)
    print(n1)
else:
    print("Fibonacci sequence:")
    while count<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
