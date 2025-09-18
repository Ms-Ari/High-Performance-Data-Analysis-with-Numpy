import numpy as np

data = np.random.randint(1, 100, size=1000)

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

matrix = data[:100].reshape(20, 5)
print("\nMatrix Sample:\n", matrix)
