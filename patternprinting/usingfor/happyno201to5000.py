num=int (input("enter the no: "))
while num !=1 and num!=4:
    sum=0
    for i in range(201,5001):
        rem=num%10
        sum+=rem*rem
        num//=10
    print(sum)
if(num==sum):
    print("it is happy no")
else:
    print("no is sad")