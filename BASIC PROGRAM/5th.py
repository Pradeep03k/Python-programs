num =2
if num%2==0:
    print("even")
else:
    print("odd")

age = int(input("Enter the Age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")



# if else 
Username = "Pradeep"
Exist_Pass = 123456 # if you store no in quotes dont take input in using data types 

takeuser = input("Enter the username: ")
userpass = int(input("Enter the password: "))

if (Username == takeuser) and (Exist_Pass == userpass):
    print("Login successfully")
else:
    print("Invalid credentials")