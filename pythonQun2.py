string_count = input("Entre a string:")
for i in string_count:
    frequency = string_count.count(i)
    print(str(i) + ":" + str(frequency))