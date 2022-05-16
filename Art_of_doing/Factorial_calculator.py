print("Welcome to the Fibonacci Calculator App")
numb = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

print("The first " + str(numb) + " numbers of the Fibonacci Sequence are: ")
fib =[1,1]
for i in range(numb-2):
    my_calc = fib[i] + fib[i+1]
    fib.append(my_calc)

for num in fib:
    print(num)

gold = []
for i in range(len(fib)-1):
    ratio = fib[i+1]/fib[i]
    gold.append(ratio)


print("\n The golden ratio values are: ")
for ratio in gold:
    print(ratio)
