# Program to filter students with marks greater than or equal to 80

students = [
    {"name": "Aarav Sharma", "marks": 78},
    {"name": "Priya Patel", "marks": 92},
    {"name": "Rohan Gupta", "marks": 65},
    {"name": "Sneha Reddy", "marks": 88},
    {"name": "Vikram Singh", "marks": 45},
    {"name": "Ananya Iyer", "marks": 95},
    {"name": "Karan Malhotra", "marks": 72},
    {"name": "Meera Nair", "marks": 81},
    {"name": "Arjun Khan", "marks": 58},
    {"name": "Ishita Joshi", "marks": 89},
]

filtered_students = [student for student in students if student["marks"] >= 80]

print("Students with Marks >= 80:")
for student in filtered_students:
    print(student)