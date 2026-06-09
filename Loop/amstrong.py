# Amstrong no 
num=int(input("Enter the no : "))
temp=num
sum=0
count=0
while temp>0:
    count+=1
    temp//=10
print(count)
temp=num
while temp>0:
    rem=temp%10
    sum+=(rem**count)
    temp//=10
print(sum)
if num == sum:
    print("it is palindrome")
else:
    print("it is not palindrome")