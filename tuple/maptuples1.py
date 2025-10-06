##Using map() and tuple()

t = (1, 2, 3, 4)
print(f"Original tuple: {t}")

# Method 1: Using map() and tuple()
squared_tuple_map = tuple(map(lambda x: x**2, t))
print(f"Squared tuple (map function): {squared_tuple_map}")