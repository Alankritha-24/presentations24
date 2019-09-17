import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#Plotting the points generated using c
P = np.loadtxt("p.dat").reshape(10,1)
Q = np.loadtxt("q.dat").reshape(10,1)
len = 10
for i in range(0,10,1):
  plt.plot(P[i][0],Q[i][0],'o')


#Plotting the line 2q-3p = 13 using python

R= np.array([-3,2])

S1 = np.array([1,0])
p = np.zeros(2)
p[0]= 13
p[1] = -5
M = np.vstack((R,S1))
A = np.dot(np.linalg.inv(M),p)


w = np.zeros(2)
w[0]= 13
w[1] = 5
M = np.vstack((R,S1))
B = np.dot(np.linalg.inv(M),w)

x_AB= line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label='$L$')

plt.grid()
plt.show()
