class BigInt:
    """
    Represents an arbitrary-precision integer

    Supports basic arithmetic operations (+, -, * //, **, and factorial)
    and conversions to/from different bases.
    """
    def __init__(self, value: str):
        """
        Initializes a BigInt object.

        Args:
        value (str): The string representation of the integer.
        The string can start with a '-' if the value is negative
        """
        self.value = BigInt.parse_value(value)

    @staticmethod
    def parse_value(value: str):
        """
        Parses a string representation of an integer into python integer.
        Handles bokth positive and negative  numbers.

        Args:
        value (str): The string representation of the integer.

        Returns:
        int: the integer parsed from the string
        """
        if value.startswith('-'):
            return -int(value[1:])
        return int(value)

    def __add__(self, other):
        """
        Adds two BigInt objects.

        Args:
        other (BigInt): The BigInt to add

        Returns:
        BigInt: A new BigInt object representing the sum.
        """
        return BigInt(str(self.value + other.value))

    def __sub__(self, other):
        """
        Subtracts another BigInt object.

        Args:
        other (BigInt): The BigInt to subtract.

        Returns:
        BigInt: A new BigInt object representing the difference.
        """
        return BigInt(str(self.value - other.value))

    def __mul__(self, other):
        """
        Multiplies two BigInt objects.

        Args:
        other (BigInt): The BigInt to multiply with.

        Returns:
        BigInt: A new BigInt object representing the product.
        """
        return BigInt(str(self.value * other.value))

    def __floordiv__(self, other):
        """
        Performs floor division (//) with another BigInt.

        Args:
        other: (BigInt): The BigInt to divide by.

        Returns:
        BigInt: A new BigInt object representingthe result of floor division.
        """
        return BigInt(str(self.value // other.value))

    def __mod__(self, other):
        """
        Calculates the modulo (%) with another BigInt object.

        Args:
        other (BigInt): The BigInt to use as the divisor.

        Retruns:
        BigInt: A new BigInt object representing the remainder.
        """
        return BigInt(str(self.value % other.value))

    def __Pow__(self, other):
        """
        Raises the BigInt to the power of another BigInt object.

        Args:
        other (BigInt): The BigInt exponent.

        Returns:
        BigInt: A new BigInt object representing the result of the exponentiaiton.
        """
        return BigInt(str(self.value ** other.value))

    def factorial(self):
        """
        Calculates the factorial of the BigInt.

        Returns:
        BigInt:  A new BigInt object representing the factorial.
        """
        result = 1
        for i in range(1, abs(self.value) + 1):
            result *= i
        return BigInt(str(result))

    def to_base(self, base):
        """
        Converts the BigInt to a string representation in the specified base.

       Args:
           base (int): The base to convert to (e.g., 2 for binary, 16 for hexadecimal).

        Returns:
            str: The string representation of the BigInt in the specified base.
        """
        n = abs(self.value)
        result = ""
        while n > 0:
            result = str(n % base) + result
            n //= base
        return ("-" if self.value < 0 else "") + result or "0"

    def from_base(self, base, representation):
        """
        Converts a number from a string representation in the specified base.

        Args:
            base (int): The base of the number (e.g., 2 for binary, 16 for hexadecimal).
            representation (str): The string representation of the BigInt in the given base.

        Returns:
            BigInt: The BigInt representation of the base representation given
        """
        return BigInt(str(int(representation, base)))

    def __str__(self):
        """
        Returns a string representation of the BigInt.

        Returns:
            str: The string representation of the BigInt value.
        """
        return str(self.value)

