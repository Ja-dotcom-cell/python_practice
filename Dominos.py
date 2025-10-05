print("Do you want (Small/Medium/Large) Pizza ? :")
size = input()

if size == "Small" or size == "small":
    bill = 100
    print("Pay 100Rs")
    print("Do you want pepperoni?(Y/N) :")
    pepperoni = input()
    if pepperoni == "Y" or pepperoni == "y":
        bill = bill + 30
        print("Your new bill is : Rs", bill)
    else:
        print("Your bill is 100Rs")

elif size == "Medium" or size == "medium":
    bill = 200
    print("Pay 200Rs")
    print("Do you want pepperoni?(Y/N) :")
    pepperoni = input()
    if pepperoni == "Y" or pepperoni == "y":
        bill = bill + 50
        print("Your new bill is : Rs", bill)

else:
    bill = 300
    print("Pay 300Rs")
    print("Do you want pepperoni?(Y/N) :")
    pepperoni = input()
    if pepperoni == "Y" or pepperoni == "y":
        bill = bill + 30
        print("Your new bill is : Rs", bill)

print("Do you need extra cheese?(Y/N) :")
cheese = input()
if cheese == "Y" or cheese == "y":
    bill = bill + 20
    print("Your new bill is : Rs", bill)
else:
    print("Thanks for visiting our store! :)")
