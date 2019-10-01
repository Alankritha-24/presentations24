import cvxpy as cp
import numpy as np

# Create two scalar optimization variables.
x = cp.Variable()
y = cp.Variable()

# Create two constraints.
constraints = [(x1)**2 + (x2)**2 <= 16,
                x1>= 0,
                x1*np.sqrt(3) + x2 >=0]

# Form objective.
obj = cp.Minimize((x1 - 1)**2 + (x2 +3)**2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x1.value, x2.value)
p = prob.value
print(np.sqrt(p))
