import math

class Polynomial():

    def __init__(self, variables):
        if isinstance(variables, (list, tuple, Polynomial)):
            self.variables = variables
        else:
            raise TypeError("Incorrect type")


    def __str__(self):
        return f'Polynomial({self.variables})'


    def __check_polynomial(self, value, operation):
        if tuple(self.variables):
            self.variables = list(self.variables)
        tmp = self.variables[-1]
        self.variables.pop(-1)
        if operation == '+':
            self.variables.append(tmp + value)
        elif operation == '-':
            self.variables.append(tmp - value)
        return self.variables


    def __check_long(self, value):
        if tuple(value):
            value = list(value)
        if len(self.variables) < len(value):
                self.variables += [0] * (len(value) - len(self.variables))
        else:
            value += [0] * (len(self.variables) - len(value))
        return self.variables, value
        

    def string_polynomial(self):
        polynomial = ''
        degree = len(self.variables) -1
        for variable in enumerate(self.variables):
            if degree == 0:
                if variable[1] < 0:
                    polynomial += ' - {}'.format(abs(variable[1]))
                else:
                    polynomial += ' + {}'.format(variable[1])
            elif degree == 1:
                if variable[0] == 0:
                    polynomial += '{}x'.format(variable[1], degree)
                else:
                    if variable[1] < 0:
                        polynomial += '- {}x'.format(abs(variable[1]))
                    else:
                        polynomial += '+ {}x'.format(variable[1])
            else:
                if variable[0] == 0:
                    polynomial += '{}x^{} '.format(variable[1], degree)
                else:
                    if variable[1] < 0:
                        polynomial += '- {}x^{} '.format(abs(variable[1]), degree)
                    else:
                        polynomial += '+ {}x^{} '.format(variable[1], degree)
            degree -= 1
        return polynomial.strip()


    def addition(self, second_polynomial):
        if isinstance(second_polynomial, (list, tuple)):
            arg1, arg2 = self.__check_long(second_polynomial)
            return [arg1[i] + arg2[i] for i in range(len(arg1))]
        elif isinstance(second_polynomial, Polynomial):
            arg1, arg2 = self.__check_long(second_polynomial.variables)
            return str(Polynomial([arg1[i] + arg2[i] for i in range(len(arg1))]))
        elif isinstance(second_polynomial, int):
            return self.__check_polynomial(second_polynomial, '+')
        else:
            raise TypeError("Incorrect type")
            

    def subtraction(self, second_polynomial):
        if isinstance(second_polynomial, (list, tuple)):
            arg1, arg2 = self.__check_long(second_polynomial)
            return [arg1[i] - arg2[i] for i in range(len(arg1))]
        elif isinstance(second_polynomial, Polynomial):
            arg1, arg2 = self.__check_long(second_polynomial.variables)
            return str(Polynomial([arg1[i] - arg2[i] for i in range(len(arg1))]))
        elif isinstance(second_polynomial, int):
            return self.__check_polynomial(second_polynomial, '-')
        else:
            raise TypeError("Incorrect type")


    def multiplication(self, second_polynomial):
        if isinstance(second_polynomial, (list, tuple)):
            rezult = [0]*(len(self.variables)+len(second_polynomial)-1)
            for o1, i1 in enumerate(self.variables):
                for o2, i2 in enumerate(second_polynomial):
                    rezult[o1+o2] += i1*i2
            return rezult
        elif isinstance(second_polynomial, Polynomial):
            rezult = [0]*(len(self.variables) +
                          len(second_polynomial.variables)-1)
            for o1, i1 in enumerate(self.variables):
                for o2, i2 in enumerate(second_polynomial.variables):
                    rezult[o1+o2] += i1*i2
            return rezult
        elif isinstance(second_polynomial, int):
            return [i*second_polynomial for i in self.variables]
        else:
            raise TypeError("Incorrect type")

    
    def isequals(self, second_polynomial):
        if isinstance(second_polynomial, (list, tuple)):
            arg1, arg2 = self.__check_long(second_polynomial)
            for i, j in zip(arg1, arg2):
                if i != j:
                    return False
                else:
                    continue
            return True
        elif isinstance(second_polynomial, Polynomial):
            arg1, arg2 = self.__check_long(second_polynomial.variables)
            for i, j in zip(arg1, arg2):
                if i != j:
                    return False
                else:
                    continue
            return True
        else:
            raise TypeError("Incorrect type")
