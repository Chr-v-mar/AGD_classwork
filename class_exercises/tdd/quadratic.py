from math import sqrt



def quadratic(a, b, c):
    if a.isinteger() and b.isinteger() and c.isinteger():
        discrim = (b ^ 2) - (4 * a * c)
        if discrim > -1:
            root1 = sqrt(discriminant**2)
            r = (-b + root1)/(2*a)
            return r
        else:
            raise ValueError("Discriminant cannot be negative")
    else:
        raise TypeError("Inputs have to be integers")
print(quadratic(1, 2, 3))