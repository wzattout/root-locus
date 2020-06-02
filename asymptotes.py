def get_sigma_a(poles_real, zeroes_real):
    sigma = 0
    for i in range(0, len(poles_real), 1):
        sigma += poles_real[i]
    for i in range(0, len(zeroes_real), 1):
        sigma -= zeroes_real[i]
    print("\u03C3 = " + str(sigma / (len(poles_real) - len(zeroes_real))) + "\n")
    return sigma / (len(poles_real) - len(zeroes_real))


def get_angles(poles_real, zeroes_real):
    angles = []
    for i in range(0, len(poles_real) - len(zeroes_real), 1):
        angles.append((2 * i + 1) * 180 / (len(poles_real) - len(zeroes_real)))
    for i in range(0, len(angles), 1):
        while angles[i] > 180:
            angles[i] -= 360
        while angles[i] < -180:
            angles[i] += 360
    print("Angles:")
    for i in range(0, len(angles), 1):
        print(angles[i])
    print(" ")
    return angles
