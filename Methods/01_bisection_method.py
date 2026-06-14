def bisection(f, a, b, tol):
    """
    Finds the root of a nonlinear equation using the Bisection Method.

    Parameters:
    f   : function (the equation f(x))
    a   : left boundary of interval
    b   : right boundary of interval
    tol : tolerance (acceptable error)

    Returns:
    Approximate root of the equation
    """

    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None

    while abs(b - a) > tol:
        c = (a + b) / 2

        if f(c) == 0:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# Function
def f(x):
    return 4*x**3 + 3*x - 3


# Call function
root = bisection(f, 0, 1, 0.05)
print("Final Root:", root)