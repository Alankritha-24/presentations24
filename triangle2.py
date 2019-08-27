from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import numpy as np

#if using termux
import subprocess
import shlex
#end if
def line_dir_pt(m,A):
  len = 10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#creating x,y for 3D plotting
xx, yy = np.meshgrid([-10,10], [-10,10])
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Equation of Plane is : n.T * x = c 



#defining line : x(k) = A + k*l
A = np.array([3,1,-1]).reshape((3,1))
l1 = np.array([-4,2,-3.33]).reshape((3,1))

B = np.array([-1,3,-4.33]).reshape((3,1))
l2 = np.array([6,-3,-0.33]).reshape((3,1))


C= np.array([5,0,-4]).reshape((3,1))
l3 = np.array([-2,1,3]).reshape((3,1))


#generating points in line 
l1_AB = line_dir_pt(l1,A)
l1_BC = line_dir_pt(l2,B)
l1_CA = line_dir_pt(l3,C)

ax.scatter(A[0],A[1],A[2],'o',label="Point A")
ax.scatter(B[0],B[1],B[2],'o',label="Point B")
ax.scatter(C[0],C[1],C[2],'o',label="Point C")


#plotting line
plt.plot(l1_AB[0,:],l1_AB[1,:],l1_AB[2,:],label="Line $AB$")
plt.plot(l1_BC[0,:],l1_BC[1,:],l1_BC[2,:],label="Line $BC$")

plt.plot(l1_CA[0,:],l1_CA[1,:],l1_CA[2,:],label="Line $CA$")


plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

#else
plt.show()
