name="Ram"
print(name)
print(id(name))
print(name[3])

name="sita"
print(name)
print(id(name))

# giving string --> fetch one by one
for ch in name:
    print(ch)

x= "maharashtra"
print(len(x))

for ch in range(len(x)-1,-1,-1):
    print(x[ch],end=" ")
print()

# count

x="india"
ct=1
for ch in x:
    ct=+1
print(ct)


# methods
x="India"
print(x.upper())
print(x.lower())

x="hello how r u ?"
print(x.title())
print(x.capitalize())

x="India"
print(x.swapcase())
print(x.replace('a','x'))

x="india"
print(x.replace('i','z'))

x="India Bharat Hidustan"
print(x.count('p'))
print(x.index('e'))
print(x.find('v'))
print(x.split(',')) 


# checking ture or false
x="india"
print(x.isupper())
print(x.islower())

# checking  all alphabets
x="hello"
print(x.isalpha())

x="1234"
print(x.isdigit())

# alphanum
x="jldjj68435"
print(x.isalnum())

# start and end
x="djdlkfjk32"
print(x.startwith("dj"))
print(x.endwith("32"))

# white spaces
x="  hello"
print(len(x))
x=x.strip()
print(len(x))




#  1 programe  without built method counting char present in string
# x="pradeep"
# print("the given string : ",x)
str=input("enter the string : ")
userinput=input("Enter which char your want : ")
count=0
for i in str:
    if i == userinput:
        count+=1
print("count : ",count)