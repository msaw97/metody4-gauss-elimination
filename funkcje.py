import numpy as np

def Doolittle(A):
    """Algorytm Doolittle'a wyswietlajacy rozklad LU macierzy"""
    n = len(A)
    L = np.zeros((n, n), dtype= np.float64)
    U = np.zeros((n, n), dtype= np.float64)
    A= A.astype(np.float64)

    for k in range(0, n):
        L[k][k]= 1

        for j in range(k, n):
            suma =0
            s=0
            while (s<=k-1):
                suma =  suma + (L[k][s]* U[s][j])
                s=s+1
            U[k][j] = A[k][j] - suma

        for i in range(k+1,n):
            suma =0
            s=0
            while (s <= k-1):
                suma = suma + (L[i][s]* U[s][k])
                s=s+1
            if U[k][k] == 0.0:
                raise ZeroDivisionError("Algorytm natrafil na zero na przekatnej.")
            else:
                L[i][k] = (A[i][k] - suma)/ U[k][k]

    return L, U

def Gauss_regular(A,B):
    """Algorytm podstawowej eliminacji Gaussa"""
    n = len(B)
    A= A.astype(np.float64)
    B= B.astype(np.float64)

    #Faza eliminacji i sprowadzenie do macierzy trojkatnej gornej
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[k][k] == 0.0:
                raise ZeroDivisionError("Algorytm natrafil na zero na przekatnej.")
            else:
                z = A[i][k]/A[k][k]
                A[i][k+1:n] = A[i, k+1:n] - z *A[k,k+1:n]
                B[i]= B[i] - z*B[k]

    #Faza podstawiania wstecz
    for k in range(n-1, -1, -1):
        if A[k][k] == 0.0:
            raise ZeroDivisionError("Algorytm natrafil na zero na przekatnej.")
        else:
            B[k]= (B[k] -np.dot( A[k,k+1:n], B[k+1:n]))/A[k,k]

    return B

def zamienW(M, i,j):
    """Funkcja pomocnicza zamienajaca porzadek wierszy"""
    if len(M.shape) == 1:
        M[i],M[j] = M[j],M[i]
    else:
        M[[i,j],:] = M[[j,i], :]

def Gauss_scaled(A, B):
    """Algorytm elimiacji gaussa z czesciowym wyborem elementow glownych"""
    n = len(A)
    S = np.zeros(n)         #skala
    P = np.array(range(n))  #permutacje
    A= A.astype(np.float64)
    B= B.astype(np.float64)

    #skala wierszy
    for i in range(n):
        S[i]= max(abs(A[i,:]))

    for k in range(0, n-1):

        #wybor elementu glownego
        for j in range(k+1, n):
            if np.abs(A[j][k])/S[j] >= abs(A[i][k])/S[i]:
                pivot =j

        #zamiana wierszy
        if pivot != k:
            zamienW(B,k,pivot)
            zamienW(S,k,pivot)
            zamienW(A,k,pivot)

        for i in range(k+1, n):
            A[k][k] = 0.0 if np.isclose(A[k][k], 0) else A[k][k]
            z = A[i][k] / A[k][k]
            A[i][k] = z

            for j in range(k+1, n):
                A[i][j] = A[i][j] - z* A[k][j]
            B[i] = B[i] - z*B[k]

    B[n-1] = B[n-1]/A[n-1,n-1]
    for k in range(n-2,-1,-1):
        A[k][k] = 0.0 if np.isclose(A[k][k], 0) else A[k][k]
        B[k] = (B[k] - np.dot(A[k,k+1:n],B[k+1:n]))/A[k,k]

    return B
