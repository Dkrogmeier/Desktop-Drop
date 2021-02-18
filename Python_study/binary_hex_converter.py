print("Welcome to the Binary/Hexadecimal Converter App")

number = int(input("\nCompute Binary and hexadecimal values up to the following decimal number: "))

decimal = list(range(1,number+1))
print(decimal)

binary = []
hexa = []

for num in decimal:
    binary.append(bin(num))
    hexa.append(hex(num))

print("\nGenerating lists....complete!\n")
dec_start = int(input("What decimal number would you like to start at: "))
dec_stop = int(input("What decimal number would you like to stop at: "))

print("\nDecimal values from " + str(dec_start) + " to " + str(dec_stop))

for i in decimal[dec_start-1:dec_stop]:
    print(i)

print("\nBinary values from " + str(dec_start) + " to " + str(dec_stop))

for i in range(dec_start-1,dec_stop):
    print(binary[i])

print("\nHexadecimal values from " + str(dec_start) + " to " + str(dec_stop))

for i in range(dec_start-1,dec_stop):
    print(hexa[i])

input("\nPress Enter to see all values from " + str(1) + " to " + str(max(decimal)) + ".")

print("\nDecimal-----Binary-----Hexadecimal")
print("----------------------------------")
for d, b, h, in zip(decimal,binary,hexa):
    print(str(d) + "-----" + str(b) + "-----" + str(h))

