n=int(input("Enter the no  :"))

for i in range(n):
    for j in range (n):
        if j==i:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
       