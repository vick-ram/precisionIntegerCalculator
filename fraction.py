class Fraction:
    """
    Represents a fraction with a denominator and numerator

    Fractions are automatically simplified upon creation.
    Supports basic representation as a string.
    """
    def __init__(self, numerator, denominator):
        """
        Initializes a Fraction Object.

        Args:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.

        Raises:
        ValueError: if the denominator is 0
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        """
        SImplifies the fraction to its lowest terms by dividing both
        the numerator and denominator by their greatest common divisor (GCD)
        """
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def gcd(a, b):
        """
        Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm

        Args:
        a (int): The first integer
        b (int): The second integer

        Returns:
        int: The GCD of a and b. The GCD is always a positive integer
        """
        while b:
            a, b = b, a % b
        return abs(a)

    def __str__(self):
        """
        Returns a string representation of the fraction in the form
        'numerator/denominator'.

        Returns:
        str: The string representation of the fraction.return
        """
        return f"{self.numerator}/ {self.denominator}"
