# 1. NO return type, no argument
def greet():
    print("welcone user")

greet()

# 2.no return type,with argument
def greet1(name):
    print("wlecome",name)

name=input("enter your name:")
greet1(name)

# 3.return type without argument
def get_no():
    return 10**2

print(get_no()) #direct print 
op=get_no()
op+=2
print(op) #using variable store

# 4. return type with argument
def cube_no(num):
    return num**3

num=int(input("enter the no:"))
# direct
print(cube(num))

# op=cube(5)
# print(op)
# 1. NO return type, no argument
# def greet():
#     print("welcone user")

# greet()

# # 2.no return type,with argument
# def greet1(name):
#     print("wlecome",name)

# name=input("enter your name:")
# greet1(name)

# # 3.return type without argument
# def get_no():
#     return 10**2

# print(get_no()) #direct print 
# op=get_no()
# op+=2
# print(op) #using variable store

# 4. return type with argument
def cube_no(num):
    return num**3

num=int(input("enter the no:"))
# direct
print(cube_no(num))

op=cube_no(5)
print(op)

 


 

