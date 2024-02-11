"""match case"""

A = int(input("Enter a number: "))

match A:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case _:
        print("No match found")
