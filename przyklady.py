import numpy as np

epsilon = 1 / (10 ** 100)

A0 = np.array([  [6,      -2,     2,       4],
                [12,     -8,     6,      10],
                [3,     -13,     9,       3],
                [-6,      4,     1,     -18]])

A1 = np.array([ [60,    30, 20,   5],   #trzy zera na przekatnej
                [30,     0, 15,  20],
                [20,    15,  0,  30],
                [10,    50, 10,  0]])

A2 = np.array([ [0,  3, -6],     #zero na pierwszym miejscu przekatnej
                [1, -6,  8],
                [3, -2, 1]])

B0 = np.array([12,   34,     27,     -38]).T

B1 = np.array([0,   1,  0]).T

B2 = np.array([2,   0,  1]).T

B3 = np.array([epsilon**(-1),   2]).T

B4 = np.array([1,   2]).T

C1 = np.array([ [epsilon,   1],     #epsilon bardzo maly na przekatnej
                [1,         1]])

C2 = np.array([ [1,              epsilon**(-1)],       #epsilon bardzo duzy w porownaniu do innych elementow macierzy
                [1,                   1]])
