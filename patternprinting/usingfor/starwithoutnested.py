num=4
for i in range(1,num+1):
    print("*"*i)


# 2nd 1234 
num=4
for i in range(1,num+1):
    for j in range(i):
        print(i,end=" ")
    print()

# 3rd reverse 
num=4
for i in range(num,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()


num=4
for i in range(1, num+1):
    if i % 2 != 0:      
        ch = '1'
    else:               
        ch = '0'

    for j in range(i):
        print(ch, end='')
    print()