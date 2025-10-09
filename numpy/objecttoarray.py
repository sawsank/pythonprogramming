import numpy as np

data = [1, 'hello', [3, 4], {'a': 5}]
obj_array = np.array(data, dtype=object)

print(obj_array)
print(type(obj_array))
