#  name star diagram 
for i in range(0,7):
    for j in range(0,5):
    
        if (j==0):
            print("*",end=" ")
        elif (i==0 or i==3) and j<4:
            print("*",end=" ")
        elif (i==1 or i==2) and j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("---------------------------------self name----------------------------------------------")

# star diagonal
for i in range (0,5):
    for j in range(0,5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        elif i==j:
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print()

print("---------------------------------star squre with diagonal ----------------------------------------------")

# star triangle upward and downward
for i in range(1,5):
    for j in range(i):
        print("* ",end=" ")
    print()
for i in range(3,0,-1):
    for j in range(i):
        print("* ",end=" ")
    print()

print("---------------------------------star with triangle ----------------------------------------------")

# star triangle up and downward odd no 
for i in range(1,5):
    num=2*i-1
    for j in range(i):
        print(num,end=" ")
    print()
for i in range(3,0,-1):
    num=2*i-1
    for j in range(i):
        print(num,end=" ")
    print()

print("---------------------------------star triangle with odd  ----------------------------------------------")
