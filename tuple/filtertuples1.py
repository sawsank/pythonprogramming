##using loop

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
print(f"Original student list: {students}")

high_achievers_loop = []
for student in students:
  if student[1] >= 90:
    high_achievers_loop.append(student)
print(f"Students with scores 90 or above (loop method): {high_achievers_loop}")