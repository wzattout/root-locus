import math


def get_departure_angles(poles_real, poles_imaginary, zeroes_real, zeroes_imaginary):
    departure_angles = []
    for i in range(0, len(poles_real), 1):
        temp = 180 - sigma_phi(poles_real, poles_imaginary, i) + sigma_zeroes(zeroes_real, zeroes_imaginary, i)
        departure_angles.append(temp)
    for i in range(0, len(departure_angles)):
        while departure_angles[i] > 180:
            departure_angles[i] -= 360
        while departure_angles[i] < -180:
            departure_angles[i] += 360
    print("Departure Angles:")
    for i in range(0, len(departure_angles)):
        print(departure_angles[i])
    print(" ")


def sigma_phi(poles_real, poles_imaginary, j):
    result = 0
    for i in range(0, len(poles_real), 1):
        if i != j:
            result += math.atan2(poles_imaginary[j] - poles_imaginary[i], poles_real[j] - poles_real[i]) * 180 / math.pi
    return result


def sigma_zeroes(zeroes_real, zeroes_imaginary, j):
    result = 0
    for i in range(0, len(zeroes_real), 1):
        if i != j:
            result += math.atan(zeroes_imaginary[i] / zeroes_real[i])
    return result * 180 / math.pi
