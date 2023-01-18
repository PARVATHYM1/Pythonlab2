tuples = ('python fullstack developer')
print(tuples)
value = input("Entre the value:")
if value in tuples:
    index = tuples.index(value)
    print("Item found at position" , index)
else:
    print("items not found at tuple")
    