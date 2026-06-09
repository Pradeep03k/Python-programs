# 1 list 
sv=int(input("enter the starting value"))
ev=int(input("enter the ending value"))

for i in range(sv,ev+1):
    if i%5==0 and i%7==0:
        print(i)



# 2 list break
for i in range(1,6):
    if i==3:
        print("thank you")
        break
    print(i)

# 3 list  skip is 4 
for i in range (1,6):
    if i==4:
        continue
    print(i)

# 4 to skip even no
for i in range (11,21):
    if i%2==0:
        continue
    print(i)

# 5 wap to print sum of no from 23 to 58
sum=0
for i in range (23,59):
    sum=sum+i

print(sum)

# 6
num=int(input("Enter the no : "))

for i in range(1,11):
    print(num ,"x" ,i, "=" ,num*i)

# 7
for i in range (501-1,102,-2):
    print(i)

# 8 find the factors 
for i in range (1,6):
    if 5%i==0:
        print(i)
# 8 2nd way
num=5
for i in range (1,6):
    if num%i==0:
        print(i)

# 9 find the factorial 
fact=1
for i in range (1,8,1):
    fact=i*fact 
print(fact)


# 9 2nd way
num=7
fact=1
for i in range (1,8,1):
    fact*=i
print(fact)

# 10 perfect no

num = int(input("enter the no : "))
sum=0
for i in range(1,num+1):
    if num % i==0:
        sum+=i 
if sum==num:
    print("perfect No ")
else:
    print("not perfect no ")

# 11 strong no 

num=int(input("enter the no : "))
temp=num
sum=0

while num>0:
    digit = num%10

    factorial=1

    for i in range(1,digit+1):

        factorial=factorial*i

    sum = sum+factorial
    num//=10

print("total=",sum)
 
if sum == temp:
    print("strong number is : ",temp)
else:
    print("it is not strong no : ",temp)
