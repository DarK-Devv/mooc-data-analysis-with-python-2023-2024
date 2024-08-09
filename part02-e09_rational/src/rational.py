import math

class Rational(object):
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        common_factor = math.gcd(numerator, denominator)
        self.numerator = numerator // common_factor
        self.denominator = denominator // common_factor

    def __add__(self, other):
        if isinstance(other, Rational):
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise ValueError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise ValueError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise ValueError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ValueError("Division by zero is not allowed")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator)
        else:
            raise ValueError("Unsupported operand type")

    def __eq__(self, other):
        if isinstance(other, Rational):
            return (self.numerator == other.numerator) and (self.denominator == other.denominator)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) < (other.numerator * self.denominator)
        else:
            raise ValueError("Unsupported operand type")

    def __gt__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) > (other.numerator * self.denominator)
        else:
            raise ValueError("Unsupported operand type")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"
