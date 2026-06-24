student=input("Enter the Name of Student : ")
sub1,sub2,sub3,sub4,sub5=map(int,input("Enter the marks of 5 subjects : ").split())

total=sub1+sub2+sub3+sub4+sub5
percentage=total/5

print("Student Name :",student)
print("Total : ",total)
print("percentage : ",percentage)


if(percentage>=90 and percentage<=100):
    print("A grade\nDistinction")
elif(percentage>=75 and percentage<90):
    print("B grade\nPass")
elif(percentage>=50 and percentage<75):
    print("C grade\nFair")
elif(percentage>0 and percentage<35):
    print("Fail")
else:
    print("invalid input\n")

