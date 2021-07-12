def factors(value):
    factors = []
    i = 2
    while i <= value:
        if value % i == 0:
            factors.append(i)
            value /= i
        else:
            i += 1
    return factors
