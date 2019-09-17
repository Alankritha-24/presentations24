#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int main() //main function begins
{

//Defining the variables
double **P,**Q,**R,**U;

//Relation between p and q is 2q-3p=13


P = loadtxt("./data/p.dat",10,1);

//Finding corresponding values of q for given values of p
U = sMul(1.5,P,10,1);
R = loadtxt("./data/r.dat",10,1);
Q = linalg_add(U,R,10,1);
saveMat(Q, "q.dat", 10, 1);


free(P);
free(R);
free(U);
free(Q);
return 0;
}
