import numpy as np

arr = np.arange(15)
result = arr[(arr >= 5) & (arr <= 10)]
print(result)