# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days_lived = int(age) * 365
weeks_lived = int(age) * 52
months_lived = int(age) * 12
limit_age_d = (90 * 365 - (days_lived))
limit_age_w = (90 * 52 - (weeks_lived))
limit_age_m = (90 * 12 - (months_lived))
print(f'You have {limit_age_d} days, {limit_age_w} weeks and {limit_age_m} months left.')
















