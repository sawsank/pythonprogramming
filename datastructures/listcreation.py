list1 = [3,6,9,12,15,18,21]
list2 = [4,8,12,16,20,24,28]
res = list()

odd_elements = list1[1::2] #Start from the 1st index with step value 2 so it will pick elements present at index 1, 3, 5, and so on
print("Elements at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2] #Start from the 0th index with step value 2 so it will pick elements present at index 0, 2, 4, and so on
print("Elements at even-index positions from list two")
print(even_elements)

print("Printing final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)