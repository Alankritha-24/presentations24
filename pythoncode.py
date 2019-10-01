import numpy as np
import matplotlib.pyplot as plt

P = np.array([-3,np.sqrt(27)])

Q = np.array([4,-np.sqrt(48)])

R = np.array([1,-3])

S = np.array([0,-7])

T = np.array([0,5])
r= 4
O = np.array([0,0])
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T

plt.plot(x_circ[0,:],x_circ[1,:],label='$C_1$')

plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.1), R[1] * (1 - 0.1) , 'R')

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
x_PQ = line_gen(P,Q)

x1 = np.linspace(0,5,100)
x2 = - x1*np.sqrt(3)


d =np.zeros((100))
plt.fill_between(x1,x2,where=x2<=d,color='grey')
x4 = np.ones((100))
x3 = 5*x4
plt.fill_between(x1,x3,where=x3>=d,color='grey')

plt.plot(x_PQ[0,:],x_PQ[1,:],label='$L1$')
x_ST = line_gen(S,T)

plt.plot(x_ST[0,:],x_ST[1,:],label='$L2$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid() 
plt.show()

  
