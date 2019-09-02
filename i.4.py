import numpy as np
import matplotlib.pyplot as plt

def sq(x):
	return x**2



#Plotting log(x)
x = np.linspace(-8,8,50)#points on the x axis
f=sq(x)#Objective function
plt.plot(x,f,color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')





plt.plot([1,5],[sq(1),sq(5)],color=(1,0,0),marker='o',label="($1$,$1$)-($5$,$25$)")
plt.plot([-1,3],[sq(-1),sq(3)],color=(0,1,0),marker='o',label="($-1$,$1$)-($3$,$9$)")
plt.plot([0,4],[sq(0),sq(4)],color=(1,1,0),marker='o',label="($0$,$0$)-($4$,$16$)")
plt.plot([-2,2],[sq(-2),sq(2)],color=(0,0,1),marker='o',label="($-2$,$4$)-($2$,$4$)")

plt.legend(loc=2)
plt.show()
