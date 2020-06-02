import math
import matplotlib.pyplot as plt
import sympy
import asymptotes
import break_away_and_crossing
import departure_angles


def daw_axises(poles_real, poles_imaginary, zeroes_real, zeroes_imaginary):
    poles_real = sorted(poles_real)
    zeroes_real = sorted(zeroes_real)
    max_x = 0
    min_x = 0
    if len(poles_real) > 0:
        max_x = poles_real[len(poles_real) - 1]
        min_x = poles_real[0]
    if len(zeroes_real) > 0:
        max_x = max(max_x, zeroes_real[len(zeroes_real) - 1])
        min_x = min(min_x, zeroes_real[0])
    max_x += 5
    min_x -= 5
    plt.plot([min_x, max_x], [0, 0])
    poles_imaginary = sorted(poles_imaginary)
    zeroes_imaginary = sorted(zeroes_imaginary)
    max_y = 0
    min_y = 0
    if len(poles_imaginary) > 0:
        max_y = poles_imaginary[len(poles_imaginary) - 1]
        min_y = poles_imaginary[0]
    if len(zeroes_imaginary) > 0:
        max_y = max(max_y, zeroes_imaginary[len(zeroes_imaginary) - 1])
        min_y = min(min_y, zeroes_imaginary[0])
    max_y += 15
    min_y -= 15
    plt.plot([0, 0], [min_y, max_y])


def draw_poles_and_zeroes(poles_real, poles_imaginary, zeroes_real, zeroes_imaginary):
    for i in range(0, len(poles_real), 1):
        plt.plot(poles_real[i], poles_imaginary[i], 'X')
    for i in range(0, len(zeroes_real)):
        plt.plot(zeroes_real[i], zeroes_imaginary[i], 'O')


def draw_asymptotes(poles_real, zeroes_real):
    x1 = asymptotes.get_sigma_a(poles_real, zeroes_real)
    angles = asymptotes.get_angles(poles_real, zeroes_real)
    plt.plot(x1, 0, 's')
    for i in range(0, len(angles), 1):
        if angles[i] < 0:
            angles[i] += 360
        y2 = 30 * math.tan(angles[i] * math.pi / 180)
        if angles[i] > 180:
            x2 = x1 - 30
        else:
            x2 = x1 + 30
        plt.plot([x1, x2], [0, y2], linestyle='--', dashes=(5, 5))


def draw_curves(poles_real, poles_imaginary):
    points = []
    equation = break_away_and_crossing.extract_equation(poles_real, poles_imaginary)
    for i in range(0, 800, 1):
        equation = equation + 5000
        points.append(sympy.solve(equation, simplify=False, rational=False))
    x = []
    y = []
    for i in range(0, len(points), 1):
        for j in range(0, len(points[i])):
            x.append(complex(points[i][j]).real)
            y.append(complex(points[i][j]).imag)
    plt.plot(x, y, '.')


def draw(poles_real, poles_imaginary, zeroes_real, zeroes_imaginary):
    daw_axises(poles_real, poles_imaginary, zeroes_real, zeroes_imaginary)
    draw_poles_and_zeroes(poles_real, poles_imaginary, zeroes_real, zeroes_imaginary)
    draw_asymptotes(poles_real, zeroes_real)
    plt.plot(break_away_and_crossing.get_break_away(poles_real, poles_imaginary), 0, 'x')
    plt.plot(0, complex(break_away_and_crossing.get_crossing()[0]).imag, 'x')
    plt.plot(0, complex(break_away_and_crossing.get_crossing()[1]).imag, 'x')
    print("Crossing with imaginary axis:")
    print(str(complex(break_away_and_crossing.get_crossing()[0]).imag) + ", " + str(complex(break_away_and_crossing.get_crossing()[1]).imag) + "\n")
    departure_angles.get_departure_angles(poles_real, poles_imaginary, zeroes_real, zeroes_imaginary)
    draw_curves(poles_real, poles_imaginary)
    plt.show()
