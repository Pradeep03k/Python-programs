# takeing user input and element in list
x=[]
print(x)
for i in range(5):
    ip=input("enter {i+1} element")
    x.append(ip)
print(x)


# extend--> 
x=[1,2]
print(x)
x.extend([3,4])
print(x)

# insert(index/value)
x=[11,13]
# 0   1-->1 2
x.insert(1,12)
print(x)

# remove(elemnet)/pop(index no)
x=[10,9,8,"hi",12,13]
x.remove("hi")
x.pop(4)
print(x)
# clear(clear entire list)
x.clear()

# count(duplicate vlaue return)
x=[10,20,10,30,40,10]
print(x.count(10))
print(x.index(30))
x.sort()
print(x)
x.reverse()
print(x)
y=x.copy()
print(y)


# function
x=[70,80,90,4,56]
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x,reverse=True))