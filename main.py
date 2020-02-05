from przyklady import *
from funkcje import *
import numpy as np

for equation in examples:
    print("Solving equation system A * X = B.\nImported example:")
    print(equation.A, " * X =", equation.B)

    print("Gauss regular solution:")
    try:
        XR = Gauss_regular(equation.A, equation.B)
        print("X: {}".format(XR))
    except ZeroDivisionError as err:
        print("Error:", err)

    print(f"Gauss scaled solution:")
    try:
        XS = Gauss_scaled(equation.A, equation.B)
        print("X: {}".format(XS))
    except ZeroDivisionError as err:
        print("Error:", err)

    print("LU decomposition of matrix A using a regular Gauss method:")
    try:
        L,U = Doolittle(equation.A)
        if not np.allclose(XS, XR):
            print("Inaccurate result when using a regular Gauss method.\n")
        else:
            print("Matrix L: \n{} \nMatrix U: \n{}\n".format(L, U))
    except ZeroDivisionError as err:
        print("Error: {}\n".format(err))
