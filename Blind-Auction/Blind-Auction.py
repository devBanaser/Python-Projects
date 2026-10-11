from art import logo1


def get_bid():
    """Ask for a bid until the user enters a whole number."""
    while True:
        bid = input("Please enter your bid in SAR: ")
        if bid.isdigit():
            return int(bid)
        print("Please enter a whole number, like 150.")


print(logo1, "\n Welcome to the blind auction.")
print("If there is a tie, the person who bid first wins.\n")

name_and_bid = {}
more_users = True

while more_users:
    name = input("Please enter your name: ")
    name_and_bid[name] = get_bid()

    add_user = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if add_user in ("no", "n"):
        more_users = False

    # Push the previous bid off screen so the next bidder can't see it
    print("\n" * 40)

# max() keeps the first highest bid it finds, so ties go to whoever bid first
max_name = max(name_and_bid, key=name_and_bid.get)
max_bid = name_and_bid[max_name]

print(f"The winner is {max_name} with a {max_bid} SAR bid.")
