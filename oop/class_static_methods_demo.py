class Calculator():
    calculation_type = "Arithmetic Operations"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return cls.a * cls.b
