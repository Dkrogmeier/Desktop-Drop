#Right Triangle Solver App
import math

print("Welcome to the Right Triangle Solver App!")

first = float(input("\nWhats the first leg of the triangle? "))
second = float(input("\nWhats the second leg of the triangle? "))

hypo = math.sqrt(first**2 + second**2)
hypo = round(hypo,3)
area = .5*first*second
area= round(area, 3)

print(hypo)
print(area)
