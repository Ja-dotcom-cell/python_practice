height=int(input("Enter Height in (integer) ft: "))
if height>3:
    print("You are eligible for ride.")
    age=int(input("Enter age :"))
    if age<12:
        print("Pay 150Rs")
    elif age<18:
        print("Pay 250Rs")
    else:
        print("Pay 500Rs")

else:
    print("You are not eligible for ride.")

    print("Have a Good Day!!")