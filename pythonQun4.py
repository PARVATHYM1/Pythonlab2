string = input("Entre a string:")
string = string.replace(" ","").lower()
repeated_character ={}
for char in string:
   if char in repeated_character:
       repeated_character[char]+=1
   else:
       repeated_character[char] = 1
count = 0
for char in repeated_character:
    if repeated_character[char]>1:
        count +=1
print("Count of repeated character:" , count)
    