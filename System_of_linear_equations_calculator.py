def Linear_Equation_System_Solver(A, B):
    m = len(A)
    assert all([len(row) == m for row in A]), "Matrix rows have non-uniform length"
    
    # Augment the matrix A with the vector B
    for i in range(m):
        A[i].append(B[i])
    
    n = m + 1  # Number of columns (including B)
    
    # Gaussian Elimination
    for k in range(m):
        # Find the k-th pivot
        i_max = max(range(k, m), key=lambda i: abs(A[i][k]))
        
        # Check for singular matrix
        if A[i_max][k] == 0:
            return []  # No unique solution
        
        # Swap rows
        A[k], A[i_max] = A[i_max], A[k]
        
        # Eliminate column below pivot
        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= A[k][j] * f
    
    # Check for inconsistency (no solution)
    for i in range(m):
        if A[i][i] == 0 and A[i][m] != 0:
            return []  # No solution
    
    # Solve equation Ax = B for an upper triangular matrix A
    x = [0] * m
    for i in range(m - 1, -1, -1):
        if A[i][i] == 0:
            return []  # No unique solution
        x[i] = A[i][m] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[i]
    
    return [round(num) for num in x]