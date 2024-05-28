



str = "Hello this is CS50"

dictionary = {}

for char in str:
    

    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1 

print(dictionary)