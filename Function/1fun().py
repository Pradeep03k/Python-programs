def print1to10():
    i=1
    while i<=10:
        print(i)
        i+=1

def table():
    num=int(input("Enter the no: "))
    i=1
    while i<=10:
        print(i*num)
        i+=1

def primeno():
    num = int(input("Enter a number: "))

    i = 2
    while i < num:
        if num % i == 0:
            print("Not Prime")
            return
        i += 1

    if num > 1:
        print("Prime")
    else:
        print("Not Prime")

while(1):
    print("1- 1 to 10 \n 2- table \n 3- primeno")
    ch=int(input("Enter the choice : "))

    if ch==1:
        print1to10()
    elif ch==2:
        table()
    elif ch==3:
        primeno()
    else:
        print("invalid choice")

    c=int(input("do you want to continue press 1 and stop press -2"))
    if c!=1:
        break

print("----------------------------------------Thank-You------------------------------------------")
