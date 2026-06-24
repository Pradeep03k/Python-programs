# manual way
x={10,20}
print(x,type(x))

# user ip
x=set()
x.add(10)
print(x,type(x))


# loop iteration
x={10,20,30,40,10,20}
print(x)
for items in x:
    print(items)
    
#methods
x.add(90)
print(x)

x.remove(40)
print(x)


# deleted element cant show error it gives perview set
x.discard(40)
print(x)

x.pop()
print(x.pop())

x.clear()
print(x)

a={1,2}
b=a.copy()
print(b)

a.update([10,20])
print(a)

# function
s={10,80,99}
print(len(s),min(s),max(s),sum(s))


# set operations(use when we handle more than two table(union,intersec,differnce,symmetric difference))

# (union = duplicate data ignore symbol(|))
a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a|b)

# intersection = common print &
print(a.intersection(b))
print(a&b)


# differnce = one table data print karne ke liye  (-)
print(a.difference(b))
print(a-b)

# symmetric difference > print all igonre commaon data (^)
print(a.symmetric_difference(b))
print(a^b)

# -----------------------------------------------------------------------------------------------------------------------


# # manual way
# x={10,20}
# print(x,type(x))

# # user ip
# x=set()
# x.add(10)
# print(x,type(x))


# # loop iteration
# x={10,20,30,40,10,20}
# print(x)
# for items in x:
#     print(items)
    
# #methods
# x.add(90)
# print(x)

# x.remove(40)
# print(x)


# # deleted element cant show error it gives perview set
# x.discard(40)
# print(x)

# x.pop()
# print(x.pop())

# x.clear()
# print(x)

# a={1,2}
# b=a.copy()
# print(b)

# a.update([10,20])
# print(a)

# # function
# s={10,80,99}
# print(len(s),min(s),max(s),sum(s))


# # set operations(use when we handle more than two table(union,intersec,differnce,symmetric difference))

# # (union = duplicate data ignore symbol(|))
# a={1,2,3}
# b={3,4,5}
# print(a.union(b))
# print(a|b)

# # intersection = common print &
# print(a.intersection(b))
# print(a&b)


# # differnce = one table data print karne ke liye  (-)
# print(a.difference(b))
# print(a-b)

# # symmetric difference > print all igonre commaon data (^)
# print(a.symmetric_difference(b))
# print(a^b)
# a


# py_std={"ram","sita","komal","ramu"}
# jv_std={"ram","pavan","gita"}
# fd_std={"gita","komal","payal","ram"}



# # total count of each
# print(len(py_std),len(jv_std),len(fd_std))
# print(len(py_std|jv_std|fd_std))
# # name of students whol are attending java and python
# print(py_std | jv_std)

# # who are attending java and python and fd
# print(py_std&jv_std&fd_std)

# # only java student 
# print(jv_std-(py_std|fd_std))

# # only python student   
# print(py_std-(jv_std|fd_std))

# # name of student who are not attending java and python
# print(fd_std-(jv_std|py_std))

# # count of student who attend 3 batch ata a time
# print(len(py_std&jv_std&fd_std))

# # name of student who attend only 1 batch at a time
# print((jv_std - (py_std | fd_std)) | (py_std - (jv_std | fd_std)) | (fd_std - (jv_std | py_std)))


# all_std=(py_std|jv_std|fd_std)
# print(len(py_std|jv_std|fd_std))
# print(all_std)
# for std in all_std:
#     count=0
#         if stud in py_std:
#             count+=1
#         if stud in jv_std:
#             count+=1
#         if stud in fd_std:
#             count+=1
#         if count == 1:
#             print(std)
            

# set eg 
set1 = {12,35,8,25,5}
set2 = {25,6,35,15,8}

# divisible by 5
all_element= set1|set2
for items in all_element:
    if items%5==0:
        print(items,end=" ")
print()   

# even sum 
sum=0
for value in all_element:
    if value%2==0:
        sum+=value
print(sum)
print()


# common element > sum of the no> then sqr > cube?
all_common=set1&set2
sum=0
sqr=0
for common in all_common:
    sum+=common
print(sum,sum**2,(sum**2)**3)

# multi of non repeted no:
non_rep=set1^set2
print(non_rep)
mul=1
for i in non_rep:
    mul*=i
print(mul)
        
