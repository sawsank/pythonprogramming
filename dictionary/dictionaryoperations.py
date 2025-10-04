my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

print(f"Original dictionary: {my_dict}")

# Remove the 'model' key-value pair using del
del my_dict['profession']
print(f"Updated dictionary after removing 'profession': {my_dict}")

print("Printing all key-value pairs:")
for key, value in my_dict.items():
  print(f"{key}: {value}")
  
def check_key_exists(dictionary, key_to_check):
  return key_to_check in dictionary

key1 = 'age'
print(f"Does '{key1}' exist? {check_key_exists(my_dict, key1)}")