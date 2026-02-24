import numpy as np
scores = np.random.randint(low = 0, high=100, size=(100,5))

average_score_student = np.mean(scores, axis=1)
average_score_subject = np.mean(scores, axis=0)
highest_score_subject = np.argmax(scores, axis = 1)

print(scores)
print(f"Average Score of each student: {average_score_student}")
print(f"Average Score of each subject: {average_score_subject}")

