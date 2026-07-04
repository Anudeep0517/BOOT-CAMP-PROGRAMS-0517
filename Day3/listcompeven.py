# Given list
numbers = [3, 7, 2, 8, 5, 10]

# List comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Display the result
print("Original List:", numbers)
print("Even Numbers:", even_numbers)