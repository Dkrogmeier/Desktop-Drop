#MPH to MPS converter

print("\nWelcome to our miles per hour to meters per second converter!")

miles = float(input("\nWhat is the MPH you would like converted? "))

convert = miles*.4474
convert = round(convert, 2)
print("Your speed is " + str(convert) + " meters per second.")
