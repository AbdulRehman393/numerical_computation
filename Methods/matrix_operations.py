import numpy as np



# ------------ Matrix Addition ------------
A = np.array([[1, 2], [3,4]])
B = np.array([[5,6],[7,8]])

result = A + B 

print("Result of A + B:\n", result)


# -------------- Matrix Subtraction ------------
import numpy as np

A = np.array([[9, 8],
              [7, 6]])

B = np.array([[1, 2],
              [3, 4]])

result = A - B

print("Result of A - B:\n", result)



# ------------ Matrix Multiplication ------------
A = np.array([[1, 2], [3,4]])
B = np.array([[5,6],[7,8]])

result = np.dot(A, B)

print("Result of A * B:\n", result)





# np.linalg.det(B)      # determinant
# np.linalg.inv(B)      # inverse
# np.dot(A, B)          # multiplication