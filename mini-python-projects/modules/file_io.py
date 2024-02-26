"""working with files"""

NAME = "My name is Manish Sharma"
PATH = "./modules/name.txt"


# with open("./modules/name.tst", "w", encoding="utf-8") as f:
#     f.write(NAME)

fp = open(PATH, "w", encoding="UTF-8")
fp.write(NAME)
fp.close()

# reading a file
with open(PATH, "r", encoding="UTF-8") as f:
    s = f.read()
    print(s)

# appending to a file
with open(PATH, "a", encoding="UTF-8") as f:
    f.write(" and I am currently exploring Python.")
