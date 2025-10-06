students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
print(f"Original student list: {students}")

# Using a list comprehension for filtering
# For each student tuple, check if their score (student[1]) is >= 90
high_achievers = [student for student in students if student[1] >= 90]
print(f"Students with scores 90 or above: {high_achievers}")