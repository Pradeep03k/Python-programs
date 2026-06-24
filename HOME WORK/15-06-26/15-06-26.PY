# 1 ST KEY VLAUE 
lst=[101,57,6,98,32,0,57,98]
userip=int(input("enter the key : "))
flag=0
for i in lst:
    if i ==  userip:
        flag=1
        break
if flag == 1:
    print("key found",i)
else:
    print("key not found")



# 2nd duplicate element print
lst=[101,57,6,98,32,0,57,98]
for i in range(len(lst)):

    for j in range(i+1,len(lst)):
        if lst[i] == lst[j]:
            print(lst[i])











# 3rd unique element print
lst=[101,57,6,98,32,0,57,98]
for i in range(len(lst)):
    count=0
    for j in range(i+1,len(lst)):
        if lst[i] == lst[j]:
            count+=1
    if count == 1:
        print("the unique elemetns :",lst[i])

# 2nd way 
lst=[101,57,6,98,32,0,57,98]
print(lst)
print("duplicate element")
for i in lst:
    if lst.count(i)==1:
        print(i)

         
# 4th without sorting
lst=[101,57,6,98,32,0,57,98]
print(len(lst))


# 5th evenodd 
lst=[101,57,6,98,32,0,57,98]
