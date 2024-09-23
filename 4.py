import numpy as np

# Create an MxN dimensional matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute the covariance matrix
cov_matrix = np.cov(matrix, rowvar=False)

# Compute the correlation matrix
corr_matrix = np.corrcoef(matrix, rowvar=False)

print(f"Covariance Matrix:\n{cov_matrix}")
print(f"Correlation Matrix:\n{corr_matrix}")
