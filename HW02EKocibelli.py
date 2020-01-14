"""
This is a Fraction Calculator Program that adds, subtracts, multiplies, divides, and checks the equality of two or more
fractions.
"""
import unittest


class Fraction:

    def __init__(self, numerator, denominator):
        """Function __init__ has the parameters that Class Fraction will use: numerator, denominator."""
        self.num = numerator
        self.den = denominator
        if denominator == 0:
            raise ZeroDivisionError("The denominator can't be zero.")

    def plus(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def minus(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def times(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        return Fraction(newnum, newden)

    def divide(self, other):
        newnum = self.num*other.den
        newden = self.den*other.num
        return Fraction(newnum, newden)

    def equal(self, other):
        if self.num*other.den == self.den*other.num:
            return True
        else:
            return False

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


def test_suite():
    """Function test_suite() tests different fractions and prints the result and the assumed result in parentheses to
    check the if the fraction class works right."""
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)
    print("Test results:")
    print(f"{f12}+{f12}={f12.plus(f12)} [4/4]")
    print(f"{f44}+{f12}={f44.minus(f12)} [4/8]")
    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f128} == {f32} is {f128.equal(f32)} [True]")
    print(f"{f12} + {f44} + {f12}= {f12.plus(f44).plus(f12)} [32/16]")

def get_int(prompt):
    """Function get_int makes sure that the user inserts an integer. If the user does not enter an integer, the exception
    catches it and prints a reminder for the user to enter an integer."""
    while True:
        value = input(prompt)
        try:
            i = int(value)
            return i
        except ValueError:
            # Handle the exception
            print("Please enter an integer")


def get_fraction():
    """Function get_fraction gets an input of numerator and denominator from the user. If user input for denominator
     is 0, is an exception and prints a reminder to the user that denominator cannot be zero."""
    while True:
        num = get_int("Enter numerator: ")
        den = get_int("Enter denominator: ")
        try:
            return Fraction(num, den)
        except ZeroDivisionError as e:
            print(e)

def get_operation():
    """Function get_operator gets an input of an operator from the user. If wrong operator prints a reminder to the user
     that the operator he/she chose is wrong. Depending on the operator user chooses, it returns the functions plus/
     minus/divide/times/equal accordingly."""
    f1 = get_fraction()

    while True:
        operation = input("Operation (+,-,*,/,==): ")
        if operation not in ['+', '-', '*', '/', '==']:
            print("Wrong OPERATION!")
        else:
            break

    f2 = get_fraction()
    if operation == '+':
        return f1.plus(f2)

    elif operation == "-":
        return f1.minus(f2)
    elif operation == "*":
        return f1.times(f2)
    elif operation == "/":
        return f1.divide(f2)
    else:
        return f1.equal(f2)


def main():
    print("Welcome to the fraction calculator!")
    result = get_operation()
    print(result)

    test_suite()


if __name__ == "__main__":
    main()
