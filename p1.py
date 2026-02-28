import numpy as np

inputs = [1, 2, 3.1]
weights = [1.2, 2.1, 3.1]
bias = 2

output = sum([i * w for i, w in zip(inputs, weights)]) + bias
print(output)

inputs = [9]
weights2 = [[1, 2, 3]]
biases = [1, 2, 2]

output = np.dot(inputs, weights) + biases
print(output)

print(np.random.rand(1, 3))
print(np.random.rand(3,1))
