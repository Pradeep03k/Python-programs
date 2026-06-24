x=(10,20,30)
print(x,type(x))
print(x[2])

for i in x:
    print(i)
    
x=("red","pink","black")
print("red" in x)
print("grey" in x)

y=(10,20)
x=(10,20,30)
print(x is y)
print(x is y)


# functions 
# len max min sort sum
print(len(x))

# methods 

# count index 
print(x.count(20))
print(x.index(30))

# slicing 
print(x[1:])
print(x[1:2])



# nested tuple
x=((10,20,),(30,40,))

for i in x:
    for j in x:
        print(j)
        
        
x=((10,20),30,(40,50),"hi")
for i in x:
    if type(i) == tuple:
        for j in i:
            print(j)
        continue
    print(i)

#conversion list into tuple and tuple into list 

x=[10,[20,30],40,(50,60)]
# print(x[2])
# print(x[3][0])
# print(x[1][1])
for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            print(j)
        continue
    print(i)


x=(90,"hi",("red",[10,20]),[100,200])

for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==list:
                for k in j:
                    print(k)
                continue
            print(j)
        continue
    print(i)




# tuple to list list to tuple
x=(10,20)
print(x,type(x))
y=list(x)
y.append(90)
print(y,type(y))
x=tuple(y)
print(x,type(x))





