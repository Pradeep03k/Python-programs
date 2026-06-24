str="python programming"
print("1-Reverse \n2-check palindorme \n3-convert string \n4-count the string \n5- Sorting the string")
userch1=int(input("Enter the user choice :"))
match userch1:
    case 1: 
        print("-------------------------------Reverse string----------------------------------------")
        print(str[::-1])
    case 2: 
        print("-------------------------------Check palindrome--------------------------------------")
        if str == str[::-1]:
            print("it is palindrome")
        else:
            print("it is not palindrome")
    case 3:
        print("-------------------------------convert string----------------------------------------")
        print("1-upper case \n2-lower case \n3-swapcase\n")
        userch2=int(input("Enter the choice :"))
        match userch2:
            case 1: 
                print(str.upper())
            case 2:
                print(str.lower())
            case 3:
                print(str.swapcase())
            case _ :
                print("invalid case")
    case 4:
        print("-------------------------------sorting string----------------------------------------")
        print(" ".join(sorted(str))) 
    case 5:
        print("-----------------------------count string---------------------------------------------")
        print("size of the string :",len(str))
    case _ :
        print("invalid case")
        

