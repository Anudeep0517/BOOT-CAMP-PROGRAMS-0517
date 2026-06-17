# Program to find the student with the highest marks

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

highest_student = max(students, key=lambda student: student["marks"])

print("Student with the Highest Marks:")
print(highest_student)