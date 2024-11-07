counter = int(input("What day are you on?: "))
counter2 = int(input("What week are you on?: "))

checker = (counter / 90) * 100
checker2 = (counter2 / 13.04) * 100

checker = round(checker, 2)
checker2 = round(checker2, 2)

print(str(counter) + "/90")
print(str(counter2) + "/13")
print("You are", str(checker) + "% done.")
print("You are", str(checker2) + "% done.")