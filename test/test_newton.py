import unittest
from numpy import sin, cos, abs
from numpy.linalg import norm
import newton

class NewtonTest(unittest.TestCase):
    def test_sin(self):
        print("sin")
        x=newton.newton(sin,cos,0.5,1e-8)
        print(sin(x))
        assert(norm(sin(x)) < 1e-8)
        #TEST CODE

    def test_polynomial(self):
        #return False
        print("polynomial")
        def f(x):
            return 3*x**3-7*x**2+x-1

        x=newton.newton(f, lambda x: 9*x**2-14*x+1, 2, 1e-8)
        print(x)
        print(f(x))
        assert(norm(f(x)) < 1e-8)


        #print("test_polynomial")
        #self.assertFalse(True)
        #TEST CODE
