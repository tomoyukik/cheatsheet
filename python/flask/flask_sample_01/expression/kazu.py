from . import expressions

class Kazu:
    def __init__(self, n):
        self.n = n

    def add(self, m):
        self.n = expressions.add(self.n, m)
        return self

    def sabtract(self, m):
        self.n = expressions.subtract(self.n, m)
        return self

    def to_int(self):
        return self.n

    def equal(self, m):
        return self.n == m