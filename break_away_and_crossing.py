import cmath
import sympy
from sympy import Symbol


def extract_equation(poles_real, poles_imaginary):
    exact_roots = []
    for i in range(0, len(poles_real), 1):
        exact_roots.append(poles_real[i] + cmath.sqrt(-1) * poles_imaginary[i])
    s = Symbol('s')
    polynomial = 1.0
    for root in exact_roots:
        polynomial *= (s - root)
    return polynomial.expand()


def get_crossing():
    routh = [[0 for x in range(3)] for y in range(4)]
    routh[0][0] = 1
    routh[0][1] = 5100
    routh[0][2] = Symbol('k')
    routh[1][0] = 125
    routh[1][1] = 65000
    routh[1][2] = 0
    routh[2][0] = ((routh[1][0] * routh[0][1]) - routh[0][0] * routh[1][1]) / routh[1][0]
    routh[2][1] = ((routh[1][1] * routh[0][2]) - routh[0][1] * routh[1][2]) / routh[1][1]
    routh[3][0] = ((routh[2][0] * routh[1][1]) - routh[1][0] * routh[2][1]) / routh[2][0]
    equation = routh[3][0].expand()
    s = Symbol('s')
    crossing = sympy.solve((routh[2][0] * s ** 2) + sympy.solve(equation)[0])
    return crossing


def get_break_away(poles_real, poles_imaginary):
    equation = Symbol.diff(extract_equation(poles_real, poles_imaginary))
    break_away_points = complex(sympy.solve(equation)[2]).real
    print("Break Away Points:")
    print(break_away_points)
    print(" ")
    return break_away_points
