counter = int(input("What day are you on?: "))
checker = (counter / 90) * 100
checker = round(checker, 2)

print(str(counter) + "/90")
print("You are", str(checker) + "% done.")