num=9
sq=num**2
sum=0

while num>0:
    rem=sq%10
    sum+=rem
    sq//=10

if num==sum:
    print("it is neon")
else:
    print("it is not neon")