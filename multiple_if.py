height=int(input("Enter Height in (integer) ft: "))
bill= 0
if height>3:
    print("You are eligible for ride.")
    age=int(input("Enter age :"))
    if age<12:
        bill = 150
        print("Pay 150Rs")
    elif age<18:
        bill = 250
        print("Pay 250Rs")
    else:
        bill = 500
        print("Pay 500Rs")

    want_photo=input("Do you want photo? (Y/N) :")
    if want_photo == "Y" or want_photo == "y" :
        print("You should add 50 Rs to your bill.")
        bill = bill + 50
        print("Your new bill is", bill)
    else:
        print("Thank you for coming here.")

else:
    print("You are not eligible for ride.")
    print("Have a Good Day!!")