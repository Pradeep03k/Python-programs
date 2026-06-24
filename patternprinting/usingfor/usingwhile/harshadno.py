num=18
sum=0

while num>0:
    # sum+=num%10
    rem=num%10    
    sum+=rem
    num//=10

if num % rem==0:
    print("it is harshad no")
else:
    print("it is not harshad")