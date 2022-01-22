def create_variables(variables):
    from sympy import symbols
    return symbols(variables, real=True)


def uncertainty(function, *variables):
    from sympy import diff
    variables = list(variables); temp = []; total = 0
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
