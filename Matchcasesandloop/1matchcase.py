print("GEO CALCI\n1.Triangle\n2.Circle\n3.Rectangle\n4.Exit")
choice=int(input("enter the choice 1: "))

match choice:
    case 1:
        print("Triangle")
        print("1.Area\n2.Perimeter\n3.Exit")
        ip1=int(input("Enter the choice 2: "))
        match ip1:
            case 1: 
                base = float(input("Enter the base: "))
                height = float(input("Enter the height: "))
                area = 0.5 * base * height
                print("Area of Triangle =", area)
            case 2:
                
                a = float(input("Enter first side: "))
                b = float(input("Enter second side: "))
                c = float(input("Enter third side: "))
                Perimeter=a+b+c
                print("Perimeter of Circle 2: ",Perimeter)
            case 3:
                print("Exit")
    case 2:
        print("circle")
        print("1.Area\n2.Circumference\n3.Exit")
        ip2=int(input("enter your choice 2: "))
        match ip2:
            case 1:
                Radius=float(input("Enter the radius of the circle : "))
                area = 3.14*Radius*Radius
                print("Area of Circle : ",area)
            case 2:
                Radius=float(input("Enter the radius of the circle : "))
                Circumference=2*3.14*Radius
                print("Circumference of Circle : ",Circumference)
            case 3:
                print("Exit")
    case 3:
        print("Rectangle")
        print("1.Area\n2.Perimeter\n3.Exit")
        ip3=int(input("Enter Your Choice 2: "))
        match ip3:
            case 1:
                length=float(input("Enter the length of the rectangle : "))
                width=float(input("Enter the width of the rectangle : "))
                area=length*width
                print("Area of Rectangle : ",area)
            case 2:
                length=float(input("Enter the length of the rectangle : "))
                width=float(input("Enter the width of the rectangle : "))
                Perimeter = 2*(length+width)
                print("Perimeter of Rectangle : ",Perimeter)
            case 3:
                print("Exit") 
    case 4:
        print("Exit")
    case 5:
        print("thank you")
    case _ :
        print("invalid input")
