class Bruch:
    def __init__(self, zaehler=1, nenner=1):
        """
        Creates a fraction using the given arguments
        0 arguments:    1 / 2,
        1 argument:     arg1 / 1,
        2 arguments:    arg1 / arg2

        :param zaehler: int
        :param nenner: int
        :raises TypeError, ZeroDivisonError
        """
        # Raise TypeError when any argument is either str or float
        if type(zaehler) is str or type(nenner) is str \
                or type(zaehler) is float or type(nenner) is float:
            raise TypeError
        # Raise ZeroDivisionError when divisor equals 0
        if nenner == 0:
            raise ZeroDivisionError

        self.zaehler = zaehler
        self.nenner = nenner

    def __abs__(self):
        """
        Returns the absolute value of the fraction
        
        :return: Bruch
        """
        self.zaehler = abs(self.zaehler)
        self.nenner = abs(self.nenner)

        return self

    def __add__(self, other):
        """
        Adds another object to this object

        :param other: Bruch, int
        :return: int, float, Bruch
        :raises: TypeError
        """
        # Raise TypeError if other is either str or float
        if type(other) is str or type(other) is float:
            raise TypeError

        if type(other) is int or type(other):
            return self.zaehler / self.nenner + other

    def __iadd__(self, other):
        """
        Adds another object to this object returning a fraction

        :param other: int, Bruch
        :return: Bruch
        """
        if type(other) is int or type(other) is float:
            self.zaehler += other * self.nenner
            return self

        return self.__add__(other)

    def __radd__(self, other):
        """
        Adds this object to another object

        :param other: int, Bruch
        :return: int, float, Bruch
        """
        return self.__iadd__(other)

    def __sub__(self, other):
        """
        Subtracts an object from this object

        :param other: Bruch, int
        :return: int, float, Bruch
        :raises: TypeError
        """
        # Raise TypeError if other is str or float
        if type(other) is str or type(other) is float:
            raise TypeError

        if type(other) is Bruch:
            z1 = self.zaehler * other.nenner
            z2 = other.zaehler * self.nenner

            self.zaehler = z1 - z2
            self.nenner *= other.nenner
            return self

    def __isub__(self, other):
        """
        Subtracts an object from this object and returns a fraction

        :param other: Bruch, int
        :return: Bruch
        """
        if type(other) is int:
            self.zaehler -= other * self.nenner
            return self

        return self.__sub__(other)

    def __rsub__(self, other):
        """
        Subtracts this object from another

        :param other: Bruch, int
        :return: int, float, Bruch
        """
        # Raise TypeError when other is float
        if type(other) is float:
            raise TypeError

        if type(other) is int:
            return other - float(self)

    def __mul__(self, other):
        """
        Multiplies this object with another returning the other objects type

        :param other: Bruch, int
        :return: int, float, Bruch
        :raises: TypeError
        """
        # Raise TypeError is other is str or float
        if type(other) is str or type(other) is float:
            raise TypeError

        if type(other) is int:
            return self.zaehler / self.nenner * other

        if type(other) is Bruch:
            self.zaehler *= other.zaehler
            self.nenner *= other.nenner
            return self

    def __imul__(self, other):
        """
        Multiplies this object with another returning a fraction

        :param other: Bruch, int
        :return: Bruch
        """
        if type(other) is int or type(other) is float:
            self.zaehler *= other
            return self

        return self.__mul__(other)

    def __rmul__(self, other):
        """
        Multiplies another object with this object returning the others type

        :param other: Bruch, int
        :return: int, float, Bruch
        """
        return self.__mul__(other)

    # Divide
    def __truediv__(self, other):
        """
        Divides this object by another object

        :param other: int, Bruch
        :return: int, float, Bruch
        :raises: ZeroDivisionError, TypeError
        """
        # Raise ZeroDivisionError if other equals to 0
        if other == 0:
            raise ZeroDivisionError
        # Raise TypeError is other is str
        if type(other) is str:
            raise TypeError

        if type(other) is int or type(other) is float:
            return self * Bruch(1, other)

        if type(other) is Bruch:
            self.zaehler *= other.nenner
            self.nenner *= other.zaehler
            return self

    def __itruediv__(self, other):
        """
        Divides this object by another returning a fraction

        :param other: int, Bruch
        :return: int, float, Bruch
        """
        if type(other) is int or type(other) is float:
            return self * Bruch(1, other)

        return self.__truediv__(other)

    def __rtruediv__(self, other):
        """
        Divides another object by this object returning the others type

        :param other: int, Bruch
        :return: int, float, Bruch
        """
        # Raise ZeroDivisionError is other is equal to 0
        if self == 0:
            raise ZeroDivisionError

        return self.__itruediv__(other)

    def __eq__(self, other):
        """
        Checks whether the value of this object is equal to the others

        :param other:
        :return: bool
        :exception: TypeError
        """
        if float(self) == float(other):
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Checks whether the value of this object is greater than the others

        :param other:
        :return: bool
        :exception: TypeError
        """
        if float(self) > float(other):
            return True

    def __ge__(self, other):
        """
        Checks whether the value of this object is greater than or equal to the others

        :param other:
        :return: bool
        :exception: TypeError
        """
        if self.__eq__(other) or self.__gt__(other):
            return True

    def __invert__(self):
        """
        Switches divisor and dividend of the fraction

        :return: Bruch
        """
        buffer = self.nenner
        self.nenner = self.zaehler
        self.zaehler = buffer

        return self

    def __pow__(self, other):
        """
        Multiplies the given fraction by itself a given number of times

        :param other: int
        :return: Bruch
        :raises: TypeError
        """
        # Raise TypeError if other is either str or float
        if type(other) is str or type(other) is float:
            raise TypeError

        if type(other) is int or type(other) is float:
            self.zaehler **= other
            self.nenner **= other

        return self

    def __ipow__(self, other):
        """
        Multiplies the given object by the value of the fraction

        :param other:
        :return:
        """
        return self.__pow__(other)

    def __neg__(self):
        """
        Multiplies the fraction with negative 1

        :return: Bruch
        """
        return self * -1

    # Casts
    def __int__(self):
        """
        Returns the value of the fraction as an integer

        :return: int
        """
        return int(float(self))

    def __float__(self):
        """
        Returns the value of the fraction as a float

        :return: float
        """
        return float(self.zaehler) / float(self.nenner)

    def __str__(self):
        """
        If the value of the fraction can be returned as an integer,
        it returns a string containing this value in round brackets.
        Otherwise the divisor and dividend are displayed, divided by a slash

        :return: str
        """
        if float(self) == int(self):
            s = "(" + str(int(self)) + ")"
        elif self.zaehler < 0 and self.nenner < 0:
            s = "(" + str(abs(self.zaehler)) + "/" + str(abs(self.nenner)) + ")"
        else:
            s = "(" + str(self.zaehler) + "/" + str(self.nenner) + ")"

        return s

    # Iteration
    def __iter__(self):
        """
        Iterates over the object yielding the divisor and then the dividend
        """
        yield self.zaehler
        yield self.nenner

    @classmethod
    def _Bruch__makeBruch(cls, value):
        """
        Returns a fraction by instantiating a new Bruch using the value as the first argument

        :param value: int
        :return: Bruch
        :raises: TypeError
        """
        if type(value) is not int:
            raise TypeError
        else:
            return Bruch(value)
z