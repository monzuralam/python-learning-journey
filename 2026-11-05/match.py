weekday = 7

match weekday:
    case 1:
        print("Saterday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thursday")
    case 7:
        print("Friday")


# default value
day = 5
match day:
    case 1:
        print("1")
    case 2:
        print("2")
    case _:
        print("fun")