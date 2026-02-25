import numpy as np

from menus import main_menu,administrative_menu


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

total_score_per_student = np.sum(scores, axis = 1)
sorted_indices = np.argsort(total_score_per_student)
top_10_indices = sorted_indices[-10:][::-1]
top_10_scores = total_score_per_student[top_10_indices]

def get_student_scores(student_number):
    if 1 <= student_number <= 100:
        return scores[student_number - 1]
    else:
        raise ValueError("Student number must be between 1 and 100.")


# print(f"Number of scores: {number_of_scores}")
# print(f"Number of students: {number_of_students}")
# print(f"Number of subjects: {number_of_subjects}")
# print(f"Average Score: {average_score}")
# print("Average Score per Subject")
# for subject, avg in zip(subjects, average_score_subject):
#     print(f"{subject}:  {avg:.2f}")
# print(f"Best Subject Score: {best_subject_score}")
# print(f"Worst Subject Score: {worst_subject_score}")
# print(f"Best Student: {best_student_loc}")
# print(f"Best Mark: {best_mark}")
# print(f"Standard Deviation: {standard_deviation}")
# print("Standard Deviation per Subject")
# for subject, std in zip(subjects, standard_deviation_subject):
#     print(f"{subject}:  {std:.2f}")
# print("Top 10 Students based on Total Scores:")
# for i, score in zip(top_10_indices, top_10_scores):
#     print(f"Student {i+1}: Total Score = {score}")



main_menu()
while True:
    try:
        choice = int(input(""))
    except ValueError:
        print(f"{choice} is an invalid input")
        
    if choice == "1":
        input = input("Pin: ")
        if input == "1234":
            print("Welcome Sir!")

            administrative_menu()
        else:
            print("Invalid Pin!!!")
            break

    elif choice == "2":
        print("Bye")
        break

    else:
        print(f"Sorry {choice} is not a valid request")
        break