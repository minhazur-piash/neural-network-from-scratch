inputs = [1, 2, 3.1]
weights = [1.2, 2.1, 3.1]
bias = 2

output = sum([i * w for i, w in zip(inputs, weights)]) + bias
print(output)
