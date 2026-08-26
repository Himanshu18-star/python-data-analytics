
#You have to plot a dashboard of 2*2 use subplots to display the following:
#1Create a bar graph to display total marks got by each students.
#2Line graph showing the marks obtained by each student in each subject.
#3Create a bar graph showing maximum and minimum marks of each subject.
#4Create a line graph showing comparison of students marks vs average marks.
import numpy as np
import matplotlib.pyplot as plt

users = np.array([
    [60, 85, 95],
    [85, 75, 90],
    [70, 80, 70]
])

students = ["Student 1", "Student 2", "Student 3"]
subjects = ["Maths", "Science", "English"]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. Bar graph - Total marks of each student
total = np.sum(users, axis=1)

axes[0, 0].bar(students, total)
axes[0, 0].set_title("Total Marks of Each Student")
axes[0, 0].set_ylabel("Marks")

# 2. Line graph - Marks in each subject
for i in range(3):
    axes[0, 1].plot(subjects, users[i], marker='o', label=students[i])

axes[0, 1].set_title("Marks in Each Subject")
axes[0, 1].set_ylabel("Marks")
axes[0, 1].legend()

# 3. Bar graph - Maximum and minimum marks of each subject
maximum = np.max(users, axis=0)
minimum = np.min(users, axis=0)

x = np.arange(3)
width = 0.35

axes[1, 0].bar(x - width/2, maximum, width, label="Maximum")
axes[1, 0].bar(x + width/2, minimum, width, label="Minimum")

axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(subjects)
axes[1, 0].set_title("Maximum and Minimum Marks")
axes[1, 0].legend()

# 4. Line graph - Student marks vs average marks
average = np.mean(users, axis=1)

axes[1, 1].plot(students, total, marker='o', label="Total Marks")
axes[1, 1].plot(students, average, marker='o', label="Average Marks")

axes[1, 1].set_title("Student Marks vs Average Marks")
axes[1, 1].set_ylabel("Marks")
axes[1, 1].legend()

plt.tight_layout()
plt.show()