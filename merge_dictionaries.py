# Program to merge two dictionaries and add values of common keys

dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))

merged = dict1.copy()

for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print("\nMerged Dictionary:")
print(merged)