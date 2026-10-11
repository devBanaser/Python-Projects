from art import logo1
print(logo1,"\n Welcome to the blind auction.")
max_bid = 0
max_name = ""
more_users = True
name_and_bid = {}
while more_users:
    name = input("Please Enter your name: ")
    bid = int(input("Please Enter your bid in SAR. (put a number and if there is a tie the person who wrote it first will win): "))
    name_and_bid[name] = bid
    add_user = input("Is there more bidders? please Enter yes or no: ")
    
    if add_user == "no":
       more_users = False

    print("\n" * 40)

for key in name_and_bid:
    if int(name_and_bid[key]) > max_bid:
        max_bid = name_and_bid[key]
        max_name = key

print(f"The winner is {max_name} with a {max_bid} SAR bid.")

    

