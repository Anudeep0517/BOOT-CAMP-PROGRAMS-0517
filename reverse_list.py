# program to reverse a given list
my_list = [1, 2, 3, 4, 5]

# Reverse the list manually
reversed_list = []

for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])

# Display the result
print("Original List:", my_list)
print("Reversed List:", reversed_list)