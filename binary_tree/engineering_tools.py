class variable:
    def __init__(self, variable):
        from sympy import symbols
        if type(variable) is list: self.variable = [symbols(variable[0], real=True)] + variable[1:]
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

    def __rpow__(self, power, modulo=None):
        if type(power) is variable:
            return power.variable[0] ** self.variable[0]
        return power ** self.variable[0]

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


def uncertainty(function, *variables, equation=False, partial_derivatives=False, show_work=False):
    from sympy import diff, acsc, asec, acot, asin, acos, atan
    from math import log as lg, e
    log = lambda x: lg(x) / lg(e)
    variables = list(variables); temp = []; work = []; total = 0
    for i, var in enumerate(variables):
        if type(var) is variable: variables[i] = var.variable
    variables.sort(key=lambda x: (len(str(x[0]))), reverse=True)
    for i in range(len(variables)):
        if equation or partial_derivatives: work.append(diff(function, variables[i][0])); continue
        if show_work: work.append(diff(function, variables[i][0]))
        temp.append(str(diff(function, variables[i][0])).replace(str(variables[0][0]), str(variables[0][1])))
        for j in range(1, len(variables)): temp[i] = temp[i].replace(str(variables[j][0]), str(variables[j][1]))
        total += eval(temp[i]) ** 2 * variables[i][2] ** 2
    if partial_derivatives: return work
    if show_work:
        for i, derivative in enumerate(work): print(f"∂g/∂{str(variables[i][0])} = {derivative}")
    stringTemp = "sqrt("
    if equation or show_work:
        for i, val in enumerate(work): stringTemp += f"({val}) ** 2 + δ{str(variables[i][0])} ** 2 + "
        stringTemp += "\b\b\b)"
        if equation: return stringTemp
        print(f"q = {stringTemp}"); stringTemp = "sqrt("
        for i in range(len(work)):
            for j in range(len(work)): work[i] = str(work[i]).replace(str(variables[j][0]), str(variables[j][1]))
        for i, val in enumerate(work): stringTemp += f"({val}) ** 2 + {variables[i][2]} ** 2 + "
        stringTemp += "\b\b\b)"
        print(f"q = {stringTemp}")
    total **= 0.5; temp = str(function).replace(str(variables[0][0]), str(variables[0][1]))
    for i in range(1, len(variables)): temp = temp.replace(str(variables[i][0]), str(variables[i][1]))
    if show_work: print(f"a = {temp}"); print(f"Answer = {eval(temp)} +- {total}"); return
    return [eval(temp), total]


def sin(expression):
    from sympy import sin
    return sin(expression * 1)


def cos(expression):
    from sympy import cos
    return cos(expression * 1)


def tan(expression):
    from sympy import tan
    return tan(expression * 1)


def csc(expression):
    from sympy import csc
    return csc(expression * 1)


def sec(expression):
    from sympy import sec
    return sec(expression * 1)


def cot(expression):
    from sympy import cot
    return cot(expression * 1)


def arcsin(expression):
    from sympy import asin
    return asin(expression * 1)


def arccos(expression):
    from sympy import acos
    return acos(expression * 1)


def arctan(expression):
    from sympy import atan
    return atan(expression * 1)


def arccsc(expression):
    from sympy import acsc
    return acsc(expression * 1)


def arcsec(expression):
    from sympy import asec
    return asec(expression * 1)


def arccot(expression):
    from sympy import acot
    return acot(expression * 1)


def log(expression, base=10):
    from sympy import log
    if type(base) is variable:
        return log(expression * 1, base * 1)
    return log(expression * 1, base)


def ln(expression):
    from sympy import log
    return log(expression * 1)


def deg_to_rad(degrees):
    from math import pi
    return degrees * pi / 180


class engineering_tools:
    class help:
        @staticmethod
        def variable():
            print("The variable type is what engineering tools uses to do its calculations")
            print("There are two ways to make a variable one as a list and one as an expression")
            print("list method: var_name = variable(['var_name', value, uncertainty])")
            print("expression method: var_name = variable('var_name = value +- uncertainty')")

        @staticmethod
        def uncertainty():
            print("This will output a list the first element being the value and the second being its uncertainty")
            print("To use you must first create variables using the variable() method")
            print("Then simply input the formula you'd like to use and then list the variables used in the equation")
            print("After listing the variables you can enable partial derivatives which will cause the function to "
                  "output the partial derivatives\nOr you can enable equation which will cause it to output "
                  "the uncertainty equation for the specified function")
            print("Example: uncertainty(x ** 3 + 2 ** cos(y), x, y)")

        @staticmethod
        def deg_to_rad():
            print("This will convert degrees into radians\n(note) the uncertainty method uses radians")

        @staticmethod
        def trig_methods():
            print("These trig methods are different from the ones found in the math module as they are compatible "
                  "with the variable() datatype")
