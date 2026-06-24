x= [[10,20],[11.2,12.3],"hi",90]
# print 12.3
print(x)        #[[10, 20], [11.2, 12.3]]
print(x[1])     #[11.2,12.3]
print(x[1][1])  #12.3
print(x[2])
print()
print("using nested list")
for i in x:
    if type(i)==list:
        for j in i:
            print(j)
        continue
    print(i)

print()
print()

x= [[10,20],[11.2,12.3],[40,50]]
# for i in x:
#     print(i[0])  
#     print(i[1])  
for i in x:
    print(f"{i[1]}-->{i[2]}")      



# orint zeroth index element 
student = [[101,"Ram",98],[102,"sita",88],[103,"ramu",78],[104,"gita",99]]
print("studen Id:")
for i in student:
    print([0])








# taking user input add student in list 
student = [[101,"Ram",98],[102,"sita",88],[103,"ramu",78],[104,"gita",99]]
student_id=int(input("enter the id:"))
student_name=input("enter the name:")
student_marks=float(input("enter the marks:"))

student.append([student_id,student_name,student_marks])
print(student)
