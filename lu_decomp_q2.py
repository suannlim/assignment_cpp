import numpy as np

def lud(A):
    
    """
    This function decomposes a given nxn matrix into the upper and lower 
    matrices.
    
    A - Input matrix to decompose
    """
    rows = len(A)
    columns = len(A[0])
    
    #checking to see if the matrix is nxn form.
    if rows!=columns:
        print("Error! This is not an nxn matrix")
        return 0
    
    # Create zero matrix with same dimensions as A
    U=[[0 for y in range(columns)] for x in range(rows)]
    L=[[0 for n in range(columns)] for m in range(rows)]
    
    for q in range(columns):
        # Set L diagonal values to 1
        L[q][q]=1 
     # For each U and L column
    for j in range(columns):
        # Loop through the column values of U
        for i in range(rows):
            # Condition to calculate value
            if i<=j:
                # Initialise a U counter
                sum_U = 0
                # This loop is for the sum in the U equation
                for k in range(i):  
                    sum_U = sum_U + (L[i][k] * U[k][j])
                U[i][j] = A[i][j] - sum_U
            else:
                continue
            
        # Loop through the column values of L
        for i in range(rows):
            # Condition to calculate value
            if i>=j:
                # Initialise a L counter
                sum_L = 0
                # This loop is for the sum in the L equation
                for k in range(j):    
                    sum_L = sum_L + (L[i][k] * U[k][j])
                L[i][j]=(A[i][j] - sum_L)/U[j][j]
            else:   
                continue
            
    return(U,L)



def determinant(U):
    """
    This function finds the determinant of a matrix using the multiplicative
    sum of the diagonal of its upper matrix.
    
    U - Upper matrix
    """
    diagonal=1
    for x in range(len(U)):
        diagonal = diagonal * U[x][x]
    print("This is the determinant " + str(diagonal))
    

def substitution(U,L,b):
    """
    This function uses forward and backwards substitution to solve the
    matrix equation.
    
    U - Upper matrix
    L - Lower matrix
    b - Solution matrix
    """
    #this function will use forward and backward substitution for the 
    #x vector 
    
    #forward substitution using L
    y=[0 for r in range(len(L))]
    for i in range(len(y)):
        y[i]=(b[i]-np.dot(y,L[i]))/L[i][i]
        
    #now backwards substitution
    x=[0 for p in range(len(U))]
    for i in reversed(range(len(U))):
        x[i]=(y[i]-np.dot(x,U[i]))/U[i][i]
    
    return x

def column(matrix,i):
    """
    This function decomposes a given matrix into the ith collumn
    
    matrix - Matrix to decompose
    i - Column number desired
    """
    return [row[i] for row in matrix]

def findInverse(A, U, L):
    """
    This function inds the inverse of a matrix using the solution of the 
    matrix equation
    
    A - Coefficient matrix
    U - Upper matrix
    L - Lower matrix
    """
    N=len(A)
    
    #Calling the identity matrix to substitute as the solution
    identityMat=np.identity(N)
    inverse=[]
    
    #Looping through each column to find the inverse of each column and column
    #stacking the results
    for i in range(N):
        b=column(identityMat,i)
        soln=substitution(U,L,b)
        inverse.append(soln)
    inverse=np.column_stack((inverse))
    print("The inverse of the original matrix is")
    print(inverse)
    return inverse
          





    
    

