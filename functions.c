//Function declaration1
double **createMat(int m,int n);
double **loadtxt(char *str,int m,int n);
double **linalg_add(double **a, double **b, int m, int n);
double **sMul(double a, double **M, int m, int n);
void saveMat(double **mat, char *str, int m, int n);
//End Function declaration


//begin function for scalar multiplication
double **sMul(double a, double **M, int m, int n)

{
int i, j;
double **c;

c = createMat(m,n);

for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
{
c[i][j]= a*M[i][j];
}
}
return c;

}
//end function for scalar multiplication

//Begin function for saving a matrix in a file
void saveMat(double** mat, char *str, int m, int n)
{
FILE *fp;
fp=fopen(str,"w");
for (int i=0; i<m; i++)
{
   for (int j=0; j<n; j++)
   {
fprintf(fp, "%lf ", mat[i][j]);
}
fprintf(fp, "\n");
}
fclose(fp);

} 

//End function for saving a matrix in a file

//Defining the function for addition of matrices

double **linalg_add(double **a, double **b, int m, int n)
{
int i, j;
double **c;
c = createMat(m,n);

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
c[i][j]= a[i][j]+b[i][j];
  }
 }
return c;

}
//End function for addition of matrices
