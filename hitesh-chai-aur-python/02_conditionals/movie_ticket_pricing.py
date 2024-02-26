user_age = int(input("\nEnter your age: "))
day = input("Are you booking for wednesday ? yes or no: ")

total_ticket_price = 0
CHILDREN_TICKET_PRICE = 8
ADULT_TICKET_PRICE = 12

if user_age >= 18:
    print(f"\nYou are an adult, ticket cost for you is ${ADULT_TICKET_PRICE}\n")
    total_ticket_price = ADULT_TICKET_PRICE
elif user_age < 19:
    print(f"\nYou are a child, it cost ${CHILDREN_TICKET_PRICE} for each ticket\n")
    total_ticket_price = CHILDREN_TICKET_PRICE


if day == "yes":
    total_ticket_price -= 2
    print(f"Final ticket price after wednesday discount is {total_ticket_price}")
