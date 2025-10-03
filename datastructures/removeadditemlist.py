sample_list = [34,54,67,89,11,43,94]

print("Original list: ", sample_list)
element = sample_list.pop(4) #pop(index): Removes and returns the item at the given index from the list.
print("After removing element at index 4: ", sample_list)

sample_list.insert(2, element) #insert(index, item): Add the item at the specified position(index) in the list
print("After adding element at index 2: ", sample_list)

sample_list.append(element) #append(item): Add the item at the end of the list
print("After adding element at last: ", sample_list)