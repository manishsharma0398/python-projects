email = input("Enter your email: ")


def error(message="Enter valid email"):
    print(message)


if (len(email) >= 6):
    print("nice")
else:
    error()
