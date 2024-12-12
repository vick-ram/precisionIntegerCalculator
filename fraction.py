class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def __str__(self):
        return f"{self.numerator}/ {self.denominator}"
