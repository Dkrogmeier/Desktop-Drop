print("Welcome to the Grade Sorter App")

grades = []
#grades.append(input("What is your first grade (0-100): ")))
#because I took the input as strings and not integers, its sorting them
#by the first number, which returns an incorrect list when given single or triple digits.
grades.append(int(input("What is your first grade (0-100): ")))
grades.append(int(input("What is your second grade (0-100): ")))
grades.append(int(input("What is your third grade (0-100): ")))
grades.append(int(input("What is your fourth grade (0-100): ")))

grades.sort(reverse = True)

print("Your grades from highest to lowest are:",end = ' ')
for i in grades:
    if i == grades[-1]:
        print(i)
    else:
        print((i), end = ', ')

print("The lowest two grades will be dropped:", end = ' ')
print(grades.pop(), end = ' ')
print(grades.pop())


print("\nYour remaining grades from highest to lowest are:",end = ' ')
for i in grades:
    if i == grades[-1]:
        print(i)
    else:
        print((i), end = ', ')
if int(grades[0]) > 80:
    print("You're crushing it! Highest grade is " + str(grades[0]))
else:
    print("You're doing your best")
