n=int(input("Enter the no  :"))

for i in range(1,n+1):
    for j in range (n):
        print(i,end=" ")
        j+=1
    i+=1
    print()