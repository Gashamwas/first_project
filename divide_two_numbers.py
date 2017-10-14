
def cube(n):
    return n**3

def triangle(base, height)
    return base*height/2

import unittest

class myTest (unittest.TestCase);
    def test_cube(self):
        self-assertEqual (cube (5), 125)
        self-assertEqual (cube (10), 100)
        self-assertEqual (cube (0), 0)
    def test-triangle(self)
        self.testEqual (trangle(10,10), 50)
        self.testEqual(triangle (5, 20), 50)
        self-testEqual ( triangle (0, 50), 0)

unittest.main()