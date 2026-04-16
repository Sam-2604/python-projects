students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

top_student = ""
top_marks = 0

for student in students:
    if students[student] > top_marks:
        top_marks = students[student]
        top_student = student

print(f"The top student is {top_student} with marks {top_marks}.")