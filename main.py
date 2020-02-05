from przyklady import *
from funkcje import *
import numpy as np

for equation in examples:
    print("Solving equation system A * X = B.\nImported example:")
    print(equation.A, " * X =", equation.B)

    print("Gauss regular solution:")
    try:
        print(f"X: {Gauss_regular(equation.A, equation.B)}")
    except ZeroDivisionError as err:
        print("Error:", err)

    print(f"Gauss scaled solution:")
    try:
        print(f"X: {Gauss_scaled(equation.A, equation.B)}")
    except ZeroDivisionError as err:
        print("Error:", err)

    print("LU decomposition of matrix A using a regular Gauss method:")
    try:
        L,U = Doolittle(equation.A)
        print("Matrix L: \n{} \nMatrix U: \n{}\n".format(L, U))
    except ZeroDivisionError as err:
        print("Error: {}\n".format(err))
