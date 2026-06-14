import numpy as np

def jacobi(A, b, x0, tol=1e-5, max_iter=100):
    """
    Solve a system of linear equations Ax = b using the Jacobi Iterative Method.

    Parameters:
    --------------------------------
    A : numpy.ndarray
        Coefficient matrix (square matrix)
    b : numpy.ndarray
        Right-hand side vector
    x0 : numpy.ndarray
        Initial guess for the solution
    tol : float
        Tolerance for stopping criteria (default = 1e-5)
    max_iter : int
        Maximum number of iterations (default = 100)

    Returns:
    --------------------------------
    numpy.ndarray
        Approximated solution vector x
    """

    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_new = np.zeros(n)

        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]

            x_new[i] = (b[i] - s) / A[i][i]

        print(f"Iteration {k+1}: {x_new}")

        # convergence check
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new

        x = x_new.copy()

    return x


# ---------------- Example ----------------

A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)

b = np.array([6, 25, -11], dtype=float)

x0 = np.zeros(len(b))

result = jacobi(A, b, x0)

print("Final Result:", result)