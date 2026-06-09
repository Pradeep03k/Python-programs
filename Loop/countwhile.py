# find the count 
# num=1234
# count=0
# while num>0:
#     count+=1
#     num//=10
# print(count)


# find the sum of the num
# num=1234
# sum=0
# while num>0:
#    rem= num%10
#    sum=sum+rem
#    num//=10
# print(sum)


# find the reverse 
# num=1234
# rev=0
# while num>0:
#    rem= num%10
#    rev=(rev*10)+rem
#    num//=10
# print(rev)


# check palindrome
num=int(input("Enter the num : "))
rev=0
original=num
while num>0:
   rem= num%10
   rev+=rem
   num//=10
if(original==rev):
   print("no is palindrome")
else:
   print("no is not palindrome")
