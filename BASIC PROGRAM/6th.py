# take 3 no from the user using if else print lagest no

n1=int(input("enter the no : "))
n2=int(input("enter the no : "))
n3=int(input("enter the no : "))

if(n1>=n2 and n1>n3):
    print(n1,"is a greatest no")
elif(n2>=n1 and n2>n3):
    print(n2,"is greatest no")
else:
    print(n3,"is greatest no")