import numpy as np

def gauss_seidel(A, b, x0, tol=1e-5, max_iter=100):
    """
    Solve Ax = b using Gauss-Seidel iterative method.

    Parameters:
    A : coefficient matrix (nxn)
    b : constant vector
    x0 : initial guess
    tol : tolerance for stopping
    max_iter : maximum iterations

    Returns:
    x : solution vector
    """

    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            s1 = 0
            s2 = 0

            # sum of already updated values
            for j in range(i):
                s1 += A[i][j] * x[j]

            # sum of old values
            for j in range(i+1, n):
                s2 += A[i][j] * x_old[j]

            x[i] = (b[i] - s1 - s2) / A[i][i]

        print(f"Iteration {k+1}: {x}")

        # convergence check
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x

    return x


# ---------------- Example ----------------

A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)

b = np.array([6, 25, -11], dtype=float)

x0 = np.zeros(len(b))

result = gauss_seidel(A, b, x0)

print("Final Result:", result)