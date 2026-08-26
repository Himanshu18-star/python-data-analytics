
import numpy as np
import pandas as pd

marks = np.array([ [85, 80, 90],     [70, 75, 65],     [92, 88, 95],     [60, 72, 68],     [78, 82, 80] ]) 

# 1. How will you calculate the total marks obtained by each student?

total_marks = np.sum(marks, axis=1)
print("Total marks obtained by each student:\n", total_marks)

# 2. How will you calculate the average marks of each student? 

average_marks = np.mean(marks, axis=1)
print("Average marks of each student: \n", average_marks)

# 4. How will you find the highest score in each subject?  
highest_scores = np.max(marks, axis=0)
print("Highest score in each subject:\n", highest_scores)

# 5. How will you find the lowest score in each subject?
lowest_scores = np.min(marks, axis=0)
print("Lowest score in each subject:\n", lowest_scores)

# 6. How will you find students whose average marks are above 80? 
students_above_80 = np.where(average_marks > 80)[0]
print("Students whose average marks are above 80:\n", students_above_80)

# 7. How will you use np.where() to assign Pass or Fail status? 
pass_fail_status = np.where(average_marks >= 50, "Pass", "Fail")
print("Pass/Fail status of each student:\n", pass_fail_status)

#8. How will you find the index of the highest-performing student? 
highest_performing_student_index = np.argmax(average_marks) 
print("Index of the highest-performing student:\n", highest_performing_student_index)

# 9. How will you calculate the standard deviation for each subject? 
standard_deviation = np.std(marks, axis=0)
print("Standard deviation for each subject:\n", standard_deviation)

# 10. How will you calculate the variance for each subject?
variance = np.var(marks, axis=0)    
print("Variance for each subject:\n", variance)

# Create the initial DataFrame
frame = pd.DataFrame(
    marks, 
    columns=['Python', 'SQL', 'MachineLearning'], 
    index=['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']
)

# Assign the new calculated columns correctly
frame[['Total Marks', 'Average Marks', 'Pass/Fail Status']] = pd.DataFrame(
    {
        'Total Marks': total_marks,
        'Average Marks': average_marks,
        'Pass/Fail Status': pass_fail_status,
    },
    index=['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']
)

print("\nFinal DataFrame with Total Marks, Average Marks, and Pass/Fail Status:\n", frame.to_string())

