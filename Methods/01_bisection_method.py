def bisection_method(func, a, b, error_accept):
    """
    This function solves for an unknown root of a non-linear function given the function,
    the initial root boundaries, and an acceptable level of error.
    """

    def f(x):
        # Using eval safely inside our wrapper function
        return eval(func)

    # 1. INITIAL CHECK: Validate boundaries before starting the loop
    if f(a) * f(b) >= 0:
        print("Bisection method fails: The function must have opposite signs at boundaries a and b.")
        return None

    error = abs(b - a)

    # 2. THE LOOP
    while error > error_accept:
        c = (b + a) / 2
        fa = f(a)
        fc = f(c)

        # Check if c is the exact root
        if fc == 0:
            a = c
            b = c
            break

        # Check which half the root lies in
        if fa * fc < 0:
            b = c  # Root is in the lower half [a, c]
        else:
            a = c  # Root is in the upper half [c, b]

        # Recalculate the error for the next iteration
        error = abs(b - a)

    print(f"The final error is {error}")
    print(f"The root is bounded between a = {a} and b = {b}")
    return a, b


# --- Test Cases ---
print("--- Test 1 ---")
bisection_method("(4*x ** 3) + 3*x -3", 0, 1, 0.05)

print("\n--- Test 2 ---")
bisection_method("(3*x ** 2) - 4", -2, 0, 0.05)