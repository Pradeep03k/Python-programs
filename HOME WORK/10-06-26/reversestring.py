# 1st without using bulit in string fun reverse string
str="hello"
count=0
for i in str:
    count+=1
print("THE COUNT OF THE STRING:",count)
for i in range(count-1,-1,-1):
    print(str[i],end=" ")

# 2nd way
str="hello"
rev=""
for ch in str:
    rev+=ch
print(rev)