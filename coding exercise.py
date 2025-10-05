#how many years,months,days we have if we live 90years old.
age=float(input("How old are you? :"))

years_left= 90-age
months_left= years_left *12
weeks_left= years_left *52
days_left= years_left *365
print(f"You have {years_left} years,{months_left}months, {weeks_left}weeks, {days_left} days left")

