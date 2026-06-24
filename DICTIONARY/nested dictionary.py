# https://www.programiz.com/online-compiler/2ENB9XsEEkLvG
stud={
    101:{
    "name": "ram",
    "age":30,
    "sub":["math","eng","java"],
    "marks":(90,89,67)
    },
    102:{
    "name": "sita",
    "age":23,
    "sub":["math","eng","java"],
    "marks":(99,80,77)
    },
    103:{
    "name": "shyam",
    "age":24,
    "sub":["math","eng","java"],
    "marks":(97,59,66)
    }
    
}
# print(stud)
# print(stud[101])
# print(stud[101]["sub"])
# print(stud[101]["sub"][2])
for key in stud:
    for v in stud[key]["marks"]:
        print(v,end=" ")
    print()


