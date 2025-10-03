from math import sqrt



def quadratic(a, b, c):
    if a.is_integer() and b.is_integer() and c.is_integer():
        if a ==0:
            raise ZeroDivisionError("Cannot divide by zero")
        discrim = (b ^ 2) - (4 * a * c)
        root1 = sqrt(sqrt(discrim ** 2))
        if root1 > -1:

            r = (-b + root1)/(2*a)
            return r
        else:
            raise ValueError("Discriminant cannot be negative")
    else:
        raise TypeError("Inputs have to be integers")
print(quadratic(1, 2, 3))