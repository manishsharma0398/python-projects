color = input("Enter colour of fruit- green, yellow, or brown :")

status = ""

match color.lower():
    case "green":
        status = "Unripe"

    case "yellow":
        status = "Ripe"

    case "brown":
        status = "Overripe"

print(f"Your fruit is {status}")
