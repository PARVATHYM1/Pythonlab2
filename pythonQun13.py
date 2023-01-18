value_list = input("Entre items for the list:")
list = list(value_list)
result = [[]]
for i in range(len(list) + 1):
    for j in range(i+1 , len(list) +1):
        sub_list = list[i:j]
        result.append(sub_list)
        
print(result)


