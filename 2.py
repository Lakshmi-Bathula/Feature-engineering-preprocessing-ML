import numpy as np

# Create two 1xM dimensional vectors
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([2, 4, 6, 8, 10])

# Compute the covariance
covariance = np.cov(vector1, vector2)[0, 1]

print(f"Covariance: {covariance}")
