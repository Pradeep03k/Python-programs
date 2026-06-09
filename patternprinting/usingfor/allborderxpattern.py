n=4
num=int(input("enter the no : "))

for i in range(num):
    for j in range(num):
        if i==1 or i==n or j==1 or j==n:
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()