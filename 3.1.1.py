import numpy as np
rows, cols = map(int, input().split())
elements = []
for _ in range(rows):
    elements.extend(map(int, input().split()))
arr = np.array(elements).reshape(rows, cols)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

