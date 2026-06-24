student = { 
    101: {
        "name": "sita",
        "sub": ["java", "python", "eng"],
        "marks": (90, 89, 78)
    },
    102: {
         "name": "ram",
         "sub": ["java", "python", "eng"],
         "marks": (90, 89, 78)
    }
}

# for key,values in student.items():
#     for key,value in values.items():
#         if type(value)==list or type(value)==tuple:
#             for

for key,value in student.items():
    for k,v in values.items():
        if v[0]=="java":
            print(v[o],key["marks"][o])
        break

for sid,details in student.items():
    for i in range(len(details["sub"])):
        if details["sub"][i]=='java':
            print(details["sub"][i],details["marks"][i],details["name"])

            if details["marks"][i]>top_marks:
                top_marks=details["marks"][i]
                top_name=details["name"]
print(f"topper name is {top_name}{top_marks}")