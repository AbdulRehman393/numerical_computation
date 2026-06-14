# 🧮 Numerical Computation Methods

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&style=flat-square)
![Methods](https://img.shields.io/badge/Methods-4%2B-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-orange?style=flat-square)

**A Python library for solving mathematical problems using numerical methods**

</div>

---

## 📚 Methods Included

### 1. **Bisection Method** - Root Finding
- Find roots of equations using interval bisection
- Simple, reliable, guaranteed convergence
- No derivative required

### 2. **Newton-Raphson Method** - Root Finding
- Fast convergence using tangent line approximation
- Requires derivative
- Excellent for smooth functions

### 3. **Jacobi Method** - Solve Linear Systems
- Iterative solver for Ax = b
- Parallelizable, good for sparse matrices
- Simple implementation

### 4. **Gauss-Seidel Method** - Solve Linear Systems
- Faster than Jacobi
- Sequential updates
- Better for dense matrices

---

## 🚀 Quick Start

### Install
```bash
git clone https://github.com/AbdulRehman393/numerical_computation.git
pip install numpy
```

### Example 1: Find Root with Bisection
```python
from Methods.bisection_method import bisection

def f(x):
    return 4*x**3 + 3*x - 3

root = bisection(f, 0, 1, tol=0.05)
print(f"Root: {root}")
```

### Example 2: Newton-Raphson
```python
from Methods.newton_raphson_method import newton_raphson

def f(x):
    return 4*x**3 + 3*x - 3

def df(x):
    return 12*x**2 + 3

root = newton_raphson(f, df, x0=0.5, tol=0.05)
print(f"Root: {root}")
```

### Example 3: Solve Linear System (Jacobi)
```python
import numpy as np
from Methods.jacobi_method import jacobi

A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)
x0 = np.zeros(len(b))

solution = jacobi(A, b, x0)
print(f"Solution: {solution}")
```

### Example 4: Gauss-Seidel
```python
from Methods.gauss_seidel_method import gauss_seidel

solution = gauss_seidel(A, b, x0)
print(f"Solution: {solution}")
```

---

## 📊 Method Comparison

| Method | Speed | Convergence | Use Case |
|--------|-------|-------------|----------|
| **Bisection** | Slow | Guaranteed | Safe, no derivative |
| **Newton-Raphson** | ⚡ Fast | Quadratic | Smooth functions |
| **Jacobi** | Moderate | Linear | Sparse matrices |
| **Gauss-Seidel** | ⚡ Faster | Linear | Dense matrices |

---

## 🔬 When to Use Each Method

```
Need to find a root?
├─ Have derivative? → Newton-Raphson ⚡
└─ No derivative? → Bisection ✅

Need to solve Ax = b?
├─ Sparse matrix? → Jacobi 📊
└─ Dense matrix? → Gauss-Seidel ⚡
```

---

## 📁 Repository Structure

```
numerical_computation/
├── README.md
└── Methods/
    ├── 01_bisection_method.py
    ├── 02_newton_raphson_method.py
    ├── 03_jacobi_method.py
    └── 04_gauss_seidel_method.py
```

---

## 🗓️ Future Additions

More methods coming soon! 🚀

---

## 💻 Requirements

```
Python >= 3.6
NumPy >= 1.19.0
```

---

## 🤝 Contributing

Want to add more methods? 
- Follow existing code structure
- Include documentation
- Add examples
- Submit a pull request!

---

## 📄 License

MIT License - Open Source

---

<div align="center">

Made with ❤️ by [AbdulRehman393](https://github.com/AbdulRehman393)

⭐ Give it a star if it helps!

</div>
