def add(a,b):
    print(a+b)
    
add(10,22)

# *args (arbiteries)
def add(*args):
    print(sum(args))
    print(type(args))
add(1,2,3,45,66)


# 
def info(name,age,marks):
    return f"name:{name}\nage:{age}\nmarks:{marks}"
    
name=input("enter a name:")
age=int(input("enter your age:"))
marks=float(input("enter your marks:"))
print(info(name,age,marks))
    
