import numpy as np


scores = np.random.randint(low=0, high=100, size=(100,5))
r , c = scores.shape
number_of_scores = r*c
number_of_students = r
number_of_subjects = c
average_score = np.mean(scores)
average_score_subject = np.mean(scores, axis = 0)


subjects = ["Programming","Math", "English", "Science", "Statistics"]
best_subject_index = np.argmax(average_score_subject)
best_subject_score = subjects[best_subject_index]


worst_subject_index = np.argmin(average_score_subject)
worst_subject_score = subjects[worst_subject_index]

average_score_student = np.mean(scores, axis = 1)
best_student_index = np.argmax(average_score_student)
best_student_loc = best_student_index + 1
best_mark = np.max(average_score_student)


standard_deviation = np.std(scores)
standard_deviation_subject = np.std(scores, axis = 0)


#Analysis:

print(f"Number of scores: {number_of_scores}")
print(f"Number of students: {number_of_students}")
print(f"Number of subjects: {number_of_subjects}")
print(f"Average Score: {average_score}")
print("Average Score per Subject")
for subject, avg in zip(subjects, average_score_subject):
    print(f"{subject}:  {avg:.2f}")
print(f"Best Subject Score: {best_subject_score}")
print(f"Worst Subject Score: {worst_subject_score}")
print(f"Best Student: {best_student_loc}")
print(f"Best Mark: {best_mark}")
print(f"Standard Deviation: {standard_deviation}")
print("Standard Deviation per Subject")
for subject, std in zip(subjects, standard_deviation_subject):
    print(f"{subject}:  {std:.2f}")