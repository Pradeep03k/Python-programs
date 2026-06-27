EMP_Name=input("enter Your Name : ")
Salary=float(input("enter Your Salary : "))
Experience=int(input("enter your Experience : "))
Performanance_rating=input("enter your Perform rating : ")

if Experience>=5 :
    Bonus=(Salary * 20)/100
elif Performanance_rating == 'A':
    Bonus=(Salary * 10)/100
elif Performanance_rating == 'B':
    Bonus=(Salary * 5)/100
else:
    print("No extra bonus")

total=Salary+Bonus

print("-------------------------SALARYSHEET-------------------------")
print("Employee Name : ",EMP_Name)
print("Salary : ",Salary)
print("performanance Rating : ",Performanance_rating)
print("Bouns on Salary : ",Bonus)
print("Total Salary : ",total)
