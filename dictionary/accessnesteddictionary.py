nested_person_dict = {'person': {'name': 'Alice', 'age': 30}}
print(f"Nested dictionary: {nested_person_dict}")

# Access Alice's age
# 1. Access the 'person' key to get the inner dictionary
# 2. Access the 'age' key within that inner dictionary
alices_age = nested_person_dict['person']['age']

print(f"Alice's age is: {alices_age}")