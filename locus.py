import numpy as np
import matplotlib.pyplot as plt

L=np.array([0,6.5])
M=np.array([-4.33,0])
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
x_LM=line_gen(L,M)
plt.plot(x_LM[0,:],x_LM[1,:],label='$line$')
plt.plot(L[0],L[1],'o')
plt.text(L[0]*(1-0.2),L[1]*(1-0.1),'L')
plt.plot(M[0],M[1],'o')
plt.text(M[0]*(1-0.1),M[1]*(1+0.2),'M')


plt.axis('equal')
plt.legend(loc='best')

plt.grid()

plt.show()
