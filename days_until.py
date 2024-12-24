import datetime

today = datetime.date.today()
print(f"Today is: {today}.")

target_year = int(input("Input year: "))
target_month = int(input("Input month number: "))
target_day = int(input("Input day number: "))

target_date = datetime.date(target_year, target_month, target_day)

result = (target_date - today).days
if result == 1:
    print(f"There is 1 day left until {target_date}.")
else:
    print(f"There are {result} days left until {target_date}.")