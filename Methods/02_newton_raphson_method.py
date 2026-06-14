def newton_raphson(f, df, x0, tol, max_iter=10):
    """
    Finds the root of a nonlinear equation using Newton-Raphson Method.

    Parameters:
    f        : function (original equation f(x))
    df       : function (derivative f'(x))
    x0       : initial guess
    tol      : tolerance (acceptable error)
    max_iter : maximum number of iterations

    Returns:
    Approximate root of the equation
    """

    x = x0

    for i in range(max_iter):
        if df(x) == 0:
            print("Derivative is zero. Method fails.")
            return None

        x_new = x - f(x) / df(x)

        print(f"Iteration {i+1}: x = {x_new}")

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return x


# Function
def f(x):
    return 4*x**3 + 3*x - 3


# Derivative
def df(x):
    return 12*x**2 + 3


# Call function
root = newton_raphson(f, df, 0.5, 0.05)
print("Final Root:", root)