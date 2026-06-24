for i in range(1,6):
    print("******************************************************************")
    print("student :",i)
    
    total=0
    
    for j in range(1,6):
        
       while True:
            marks = int(input(f"Enter marks of subject {j}: "))

            if marks >=0 and  marks <=100:
                total += marks
                break
            else:
                print("Invalid marks! Please enter marks between 0 and 100.")
    
    percentage=total/5
    
    print("------------------------------------------------------------------")
    if percentage >90 :
        Grade='A+'
    elif percentage >75:
        Grade='A'
    elif percentage >60:
         Grade='B'
    elif percentage >=35:
         Grade='C'
    else:
         Grade="Fail"
    print("----------------------------Marksheet-----------------------------")
    print("Total Marks =", total)
    print("Percentage =", percentage)
    print("Grade =", Grade)
print()

        