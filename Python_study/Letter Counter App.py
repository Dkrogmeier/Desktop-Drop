
print('Welcome to the letter counter app!')

intro = input("\nBefore we get started, what is your name: ").title().strip()
print("\nHello " + intro + "!\nI will count the number of letters in your message!")

message = input("\nPlease enter a message:").lower()
letter = input("Which letter would you like to count:").lower()
countMe = message.count(letter)
print("Your message has " + str(countMe)+ " " + letter + "'s, " + intro + ".")

