angle1, angle2, angle3 = map(int, input("Enter 3 angles: ").split())

if angle1+angle2+angle3==180:
    
    if angle1==angle2==angle3:
        print("eqvilatral Triangle")
    elif angle1==angle2 or angle2==angle3 or angle1==angle3:
        print("isolatral")
    else:
        print("Scalene Triangle")
else:
    print("invlaid Triangle")