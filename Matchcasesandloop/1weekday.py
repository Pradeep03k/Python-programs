day=int(input("enter the day to check betn (1-7) : "))
match day:
    case 1|2|3|4|5:
        print("weekday")
    case 6|7:
        print("weekend")
    case _:
        print("invalid choice")