import cvxpy as cp
import numpy as np

# Create two scalar optimization variables.
x = cp.Variable()
y = cp.Variable()

# Create two constraints.
constraints = [(x)**2 + (y)**2 <= 16,
                x>= 0,
                x*np.sqrt(3) + y >=0]

# Form objective.
obj = cp.Minimize((x - 1)**2 + (y+3)**2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)
p = prob.value
print(np.sqrt(p))
