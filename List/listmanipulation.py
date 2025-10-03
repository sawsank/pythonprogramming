my_list = [10, 20, 30, 40, 50]
print("Initial list:", my_list)

# Change the second element (at index 1) to 200
my_list[1] = 200
print("After changing second element:", my_list)

# Add 600 to the end of the list
my_list.append(600)
print("List after appending 600:", my_list)

# Insert 300 at index 2
my_list.insert(2, 300)
print("List after inserting 300 at index 2:", my_list)

# Remove 600 from the list (by value)
my_list.remove(600)
print("List after removing 600 (by value):", my_list)

# Remove the element at index 0 (using del)
del my_list[0]
print("List after removing element at index 0:", my_list)