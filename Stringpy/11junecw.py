x="india"
print(x[3:5])
print(x[3:])
print(x[0:3])
print(x[:3])
print(x[0:5:2])

x="india is my country"
print(len(x))
print(x[6:8])
print(x[12:17])
print(x[7:10])
print(x[16:19])
print(x[-9:-15:-1])
print(x[-1:-20:-1])
print(x[0:19])

# reversing 
print(x[::-1])

11
ip=input("Enter the string: ")
if ip==ip[::-1]:
    print("plaindorme")
else:
    print("not palindrome")


12

x="abc123345"
ctdigit=0
ctchar=0
for ch in x:
    # if (ch>='0' and ch<='9'):
    #     ctdigit+=1
    # elif(ch>='a'and ch<='z' or ch>='A'and ch<='Z'):
    #     ctchar+=1
    
    if ch.isdigit():
        ctdigit+=1
    elif ch.isalpha():
        ctchar+=1
print(ctdigit)
print(ctchar)
print(f"count of digit {ctdigit}\n count of char {ctchar}")


# ord 3
x="swapcase"
store=""
for i in x:
    if i >= 'a' and i <='z':
        store+=chr(ord(i)-32)
print(store)

# ord eg 
x="sWapCase"
store1=""
store2=""
for i in x:
    if i >= 'a' and i <='z':
        store1+=chr(ord(i)-32)
    elif i >= 'A' and i <= 'Z':
        store2+=chr(ord(i)+32)
print(f"store1 char is : {store1}\nstore2 char is : {store2}")


# home work 10 june

x="programming"
# even
for i in x:
    if ord(i)%2==0:
        print(i,ord(i))
        
        
        
# whitespace
x=" hey"
print(len(x))
new=""
for ch in x:
    if ' ' not in ch:
        new+=ch
print("ans",new,len(new))




# programming
x="programming"
unique=""
for ch in x:
    if ch not in unique:
        unique+=ch
        print("flow understand :",unique)
print("final ans:",unique)


# eg

x="I Like python programming"
store=0
for ch in x:
    if ' 'in ch:
        store+=1
print(store)






