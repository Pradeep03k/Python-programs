# 1st 

for i in range(1,4):
    for j in range(1,4):
        
        if (i+j)%2==0: 
            print("X",end=" ")
        else:
            print("O",end=" ")
    print()
    
print("----------------------xoxo----------------------------")

# 2nd
for i in range(1,4):
    ch=chr(96 + i)
    for j in range(1,4):
        print(ch,end=" ")
    print()
    
print("------------------------abc---------------------------")

# 3rd
ch = 97

for i in range(1, 4):
    for j in range(1, 5):

        print(chr(ch), end=" ")

        ch += 1
    print()
    
print("-----------------------atol-----------------------------")


# 4th
for i in range(1, 4):

    num = 1

    for j in range(1, 4):
        print(num, end=" ")
        num += 1

    print()

print("-----------------------123------------------------------")


# 5th
num = 9
for i in range (1,4):
    for j in range(1,4):
        print(num,end=" ")
        num -=1
    print()
    
print("-----------------------9 to 1 ------------------------------")

ch = 65   # ASCII of 'A'


#6th
for i in range(1, 4):
    for j in range(1, 4):
        print(chr(ch), end=" ")
        ch += 2
    print()
    
print("-----------------------alpha even-------------------------------")

# 7th
for i in range(1, 5):
    for j in range(1, 5):

        if i == 1 or i == 4 or j == 1 or j == 4:
            
            # corners
            if (i == 1 and j == 1) or (i == 1 and j == 4) or (i == 4 and j == 1) or (i == 4 and j == 4):
                print("O", end=" ")
            else:
                print("X", end=" ")
        
        else:
            print(" ", end=" ")

    print()

print("-------------------------oxox all border---------------------------------------")

#8
for i in range (1,6):
    for j in range(1,6):
        if i==1 or i == 5 or j==1 or j == 5 or (i==3 and j == 3):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
        