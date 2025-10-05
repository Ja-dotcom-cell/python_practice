import random

dice_side = random.randint(1,6)
if dice_side == 1:
    print("Not 6")
elif dice_side == 2:
    print("Not 6")
elif dice_side == 3:
    print("Not 6")
elif dice_side == 4:
    print("Not 6")
elif dice_side == 5:
    print("Not 6")
else:
    print("Congrats it's a 6!")

#i run this code 100 times to see how many times 6 will appear, i saw just 15 times
# 6 appears, so the probability of getting 6 : 15 / 100 = 0.15 = 15%