student={}


while(True):
            
            print("1.Add\n2.view\n3.total")
            choice=int(input("enter the choice:"))
            match choice:
                    case 1:
                        # add 
                        ip=int(input("enter how many student do u wnat:"))
                        for i in range(ip):
                            print("-------------------------------------student-details-----------------------------------------------------\n")
                            sid=int(input("enter student id:"))
                            name=input("enter the name of student:")
                            sub_value=input("enter subject name:").split()
                            marks_value=tuple(map(int,input("enter student marks:")).split())
                            student [sid] ={
                                "name":name,
                                "sub":sub_value,
                                "marks":(marks_value)
                            }
                    case 2: 
                          for sid,details in student.items():
                                 print(f"student id:{sid}\nstudent name:{details['name']}\nstudent sub:{details['sub']}\nstudent marks:{details['marks']}")
                    
                    case 3:
                        # total marks and percentage
                        for key in student:
                              total=0
                              percentage=0.0
                              for value in student[key]["marks"]:
                                    total+=value
                                    percentage=total/3
                              print(total,percentage)
                    case 4:
                        
                          

    
     
     