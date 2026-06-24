# def add(a,b):
#     print(a+b)
    
# add(10,22)

# # *args (arbiteries)
# def add(*args):
#     print(sum(args))
#     print(type(args))
# add(1,2,3,45,66)


# # 
# def info(name,age,marks):
#     return f"name:{name}\nage:{age}\nmarks:{marks}"
    
# name=input("enter a name:")
# age=int(input("enter your age:"))
# marks=float(input("enter your marks:"))
# print(info(name,age,marks))
    
def addition():
        a=int(input("enter a no:"))
        b=int(input("enter a no:"))
        print("Addtion of no: ",a+b)

def subtraction():
        a=int(input("enter a no:"))
        b=int(input("enter a no:"))
        print("substraction of no: ",a-b)

def multiplication():
        a=int(input("enter a no:"))
        b=int(input("enter a no:"))
        print("Multiplication of no: ",a*b)

def Division():
        a=int(input("enter a no:"))
        b=int(input("enter a no:"))
        print("Division of no: ",a//b)
    
def remainder():
        a=int(input("enter a no:"))
        b=int(input("enter a no:"))
        print("Remainder of no: ",a%b)
    
print("1.Addition\n2.Substraction\n3.multiplication\n4.Division\n5.Remiander\n")
choice=int(input("enter your choice"))

match choice:
        case 1:
            addition()
        case 2:
            subtraction()
        case 3:
            multiplication()
        case 4:
            Division()
        case 5:
            remainder()
        case _ :
            print("invalid condition")