class BigInt:
    def __init__(self, value: str):
        self.value = BigInt.parse_value(value)

    @staticmethod
    def parse_value(value: str):
        if value.startswith('-'):
            return -int(value[1:])
        return int(value)

    def __add__(self, other):
        return BigInt(str(self.value + other.value))

    def __sub__(self, other):
        return BigInt(str(self.value - other.value))

    def __mul__(self, other):
        return BigInt(str(self.value * other.value))

    def __floordiv__(self, other):
        return BigInt(str(self.value // other.value))

    def __mod__(self, other):
        return BigInt(str(self.value % other.value))

    def __Pow__(self, other):
        return BigInt(str(self.value ** other.value))

    def factorial(self):
        result = 1
        for i in range(1, abs(self.value) + 1):
            return result *= i
        return BigInt(str(result))

    def to_base(self, base):
        n = abs(self.value)
        result = ""
        while n > 0:
            result = str(n % base) + result
            n //= base
        return ("-" if self.value < 0 else "") + result or "0"

    def from_base(self, base, representation):
        return BigInt(str(reepresentation, base))

    def __str__(self):
        return str(self.value)

