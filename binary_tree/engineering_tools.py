class variable:
    def __init__(self, variable):
        from sympy import symbols
        if type(variable) is list: self.variable = [symbols(self, real=True)] + variable[1:]
        if type(variable) is not str:
            return
        self.variable = variable.split("=")
        self.variable[1:] = self.variable[1].split("+-")
        self.variable = [i.strip() for i in self.variable]
        for i, var in enumerate(self.variable):
            try: self.variable[i] = float(var)
            except ValueError: self.variable[i] = symbols(var)

    def __str__(self):
        return str(self.variable)

    def __repr__(self):
        return self.variable

    def __neg__(self):
        return self.variable[0] * -1

    def __abs__(self):
        return abs(self.variable[0])

    def __pow__(self, power, modulo=None):
        if type(power) is variable:
            return self.variable[0] ** power.variable[0]
        return self.variable[0] ** power

    def __mul__(self, other):
        if type(other) is not variable:
            return self.variable[0] * other
        return self.variable[0] * other.variable[0]

    def __rmul__(self, other):
        if type(other) is not variable:
            return self.variable[0] * other
        return self.variable[0] * other.variable[0]

    def __truediv__(self, other):
        if type(other) is not variable:
            return self.variable[0] / other
        return self.variable[0] / other.variable[0]

    def __rtruediv__(self, other):
        if type(other) is not variable:
            return other / self.variable[0]
        return other.variable[0] / self.variable[0]

    def __add__(self, other):
        if type(other) is not variable:
            return self.variable[0] + other
        return self.variable[0] + other.variable[0]

    def __radd__(self, other):
        if type(other) is not variable:
            return self.variable[0] + other
        return self.variable[0] + other.variable[0]

    def __sub__(self, other):
        if type(other) is not variable:
            return self.variable[0] - other
        return self.variable[0] - other.variable[0]

    def __rsub__(self, other):
        if type(other) is not variable:
            return other - self.variable[0]
        return other.variable[0] - self.variable[0]

    def __floordiv__(self, other):
        if type(other) is not variable:
            return self.variable[0] // other
        return self.variable[0] // other.variable[0]

    def __rfloordiv__(self, other):
        if type(other) is not variable:
            return other // self.variable[0]
        return other.variable[0] // self.variable[0]

    def __mod__(self, other):
        if type(other) is not variable:
            return self.variable[0] % other
        return self.variable[0] % other.variable[0]

    def __rmod__(self, other):
        if type(other) is not variable:
            return other % self.variable[0]
        return other.variable[0] % self.variable[0]


def uncertainty(function, *variables):
    from sympy import diff
    variables = list(variables); temp = []; total = 0
    for i, var in enumerate(variables):
        if type(var) is variable: variables[i] = var.variable
    for i in range(len(variables)):
        temp.append(str(diff(function, variables[i][0])).replace(str(variables[0][0]), str(variables[0][1])))
        for j in range(1, len(variables)): temp[i] = temp[i].replace(str(variables[j][0]), str(variables[j][1]))
        total += eval(temp[i]) ** 2 * variables[i][2] ** 2
    total **= 0.5; return total


def sin(expression):
    from sympy import sin
    return sin(expression)


def cos(expression):
    from sympy import cos
    return cos(expression)


def tan(expression):
    from sympy import tan
    return tan(expression)


def csc(expression):
    from sympy import csc
    return csc(expression)


def sec(expression):
    from sympy import sec
    return sec(expression)


def cot(expression):
    from sympy import cot
    return cot(expression)


def arcsin(expression):
    from sympy import asin
    return asin(expression)


def arccos(expression):
    from sympy import acos
    return acos(expression)


def arctan(expression):
    from sympy import atan
    return atan(expression)


def arccsc(expression):
    from sympy import acsc
    return acsc(expression)


def arcsec(expression):
    from sympy import asec
    return asec(expression)


def arccot(expression):
    from sympy import acot
    return acot(expression)


def deg_to_rad(degrees):
    from math import pi
    return degrees * pi / 180
