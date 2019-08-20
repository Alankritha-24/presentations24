# presentations24
import numpy as np
import matplotlib.pyplot as plt

import subprocess
import shlex

M = np.array([1,2])
N = np.array([-3,4])
Q = np.array([4,3])
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x_MN = line_gen(M,N)
plt.plot(x_MN[0,:],x_MN[1,:],label='$MN$')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.1), M[1] * (1 - 0.1) , 'M')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1 + 0.1), N[1] * (1 - 0.1) , 'N')

m = M-N
o1 = np.array([0,1])
o2 = np.array([-1,0])
omat = np.vstack((o1,o2))


#print(m)

n = np.dot(omat,m)
print(n)

p = np.zeros(2)
p[0] = np.dot(n,M)
p[1] = np.dot(m,Q)

#print(p)

d = np.vstack((n,m))
P = np.dot(np.linalg.inv(d),p)

#print(P)

m1 = np.array([1,0])
m2 = np.array([0,1])

h= np.dot(m1,P)
k = np.dot(m2,P)

#print(k/h)

x_MP = line_gen(M,P)
plt.plot(x_MP[0,:],x_MP[1,:],label='$MP$')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')

x_QP = line_gen(Q,P)
plt.plot(x_QP[0,:],x_QP[1,:],label='$QP$')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.1), Q[1] * (1 - 0.1) , 'Q')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('equal')
plt.legend(loc="best")
plt.grid()
plt.show()

plt.savefig('../figs/presentation.pdf')

subprocess.run(shlex.split("termux-open ../figs/presentation.pdf"))

