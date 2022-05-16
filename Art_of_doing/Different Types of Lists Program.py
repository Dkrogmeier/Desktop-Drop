#Different types of lists Program

num_strings = ["15","100","20"]
num_ints = [100, 15, 20]
num_floats = [2.2, 3.6, 1.235]
num_lists = [num_strings, num_ints, num_floats]

print(type(num_strings))
print(type(num_ints))
print(type(num_floats))
print(type(num_lists))


print(num_strings)
print(num_ints)
print(num_floats)
print(num_lists)


print(type(num_strings[0]))
print(type(num_ints[0]))
print(type(num_floats[0]))
print(type(num_lists[0]))

num_strings.sort()
num_ints.sort()

print(num_strings)
print(num_ints)
print(num_lists[0])
print(num_lists[1])
print(num_lists[2])
