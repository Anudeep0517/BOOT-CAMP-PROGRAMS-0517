# program to find no of even and odd numbers present in list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of Even Numbers:", even_count)
print("Number of Odd Numbers:", odd_count)