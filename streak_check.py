def streak_check():
    day = int(input("What day are you on?: "))
    week = int(input("What week are you on?: "))

    day_check = (day / 90) * 100
    week_check = (week / 13.04) * 100

    day_check = round(day_check, 2)
    week_check = round(week_check, 2)

    print()
    print("Day", str(day) + "/90")
    print("Week", str(week) + "/13")
    print("You are", str(day_check) + "% done day-wise.")
    print("You are", str(week_check) + "% done week-wise.")

streak_check()