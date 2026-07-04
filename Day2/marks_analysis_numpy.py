#dataset

import numpy as np
np.random.seed(0)
marks = np.random.randint(35, 100, size=(100, 5))

print("Dataset:\n", marks)

# shape and dimensions

print("\nShape:", marks.shape)
print("Dimensions:", marks.ndim)
print("Total Elements:", marks.size)

# Slicing

print("\nFirst Student:", marks[0, :])
print("Math Column:", marks[:, 0])
print("First 5 Students:\n", marks[0:5, :])
print("Physics & Chemistry:\n", marks[:, 1:3])
print("Specific Students:\n", marks[[0, 10, 25], :])
print("Marks > 90:", marks[marks > 90])

# Vectorized operations

print("\nAdd Grace (+5):\n", marks + 5)
print("Increase Math by 10:\n", marks[:, 0] + 10)
print("Squared Marks:\n", marks ** 2)

# Normalize Math column
math_marks = marks[:, 0]
normalized = (math_marks - np.mean(math_marks)) / np.std(math_marks)
print("Normalized Math Marks:\n", normalized)

# 5. Advanced Vectorization

weights = np.array([1.0, 0.9, 0.8, 0.7, 1.2])
weighted_marks = marks * weights
print("\nWeighted Marks:\n", weighted_marks)

total = np.sum(marks, axis=1)
print("Total per Student:\n", total)

avg_subject = np.mean(marks, axis=0)
print("Average per Subject:\n", avg_subject)

# Analysis tasks

topper_index = np.argmax(total)
print("\nTopper Index:", topper_index)

subject_toppers = np.argmax(marks, axis=0)
print("Topper in Each Subject:", subject_toppers)

print("Failures (<40):", marks[marks < 40])

avg_student = np.mean(marks, axis=1)
high_performers = marks[avg_student > 75]
print("High Performers:\n", high_performers)



