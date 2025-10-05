name_1 = input("What is his name :")
name_2 = input("What is her name :")
combine_str = name_1 + " " + name_2
lower_case_str = combine_str.lower()

t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e = lower_case_str.count("e")

true = t + r + u + e

l= lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e = lower_case_str.count("e")

love= l + o + v + e
love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90 :
    print("Your love score is", love_score,"%. Go for cokes & mentos.")
elif love_score >= 40 or love_score <= 50 :
    print("Your love score is", love_score,"%. You are alright together.:V")
else:
    print("You two are good.Best of luck!")
