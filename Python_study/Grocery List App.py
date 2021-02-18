#Grocery List App
import datetime

print("Welcome to our Grocery List App")

Glist = ["Meat","Cheese"]

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print(time)

print("Your current list is " + str(len(Glist))+  " items long and includes: ", end = ' ')
for i in Glist:
    if i == Glist[-1]:
        print(i, end = ' ')
    else:
        print(i, end = ', ')

Glist.append(input("\nWhat else would you like to add? ").title())

print("Your current list is " + str(len(Glist))+  " items long and includes: ", end = ' ')
for i in Glist:
    if i == Glist[-1]:
        print(i, end = '\n')
    else:
        print(i, end = ', ')


for i in Glist:
    if i == Glist[-2]:
        print("The store didnt have " + i)
        Glist.append(input("What would you like instead? ").title())
    else:
        print("You bought " + i)
        print("Removing " + i + " from the list")
        Glist.remove(i)
        
print("Your current list is " + str(len(Glist))+  " items long and includes: ", end = ' ')
for i in Glist:
    if i == Glist[-1]:
        print(i, end = ' ')
    else:
        print(i, end = ', ')              
