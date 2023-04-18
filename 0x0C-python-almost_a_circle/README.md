A simple Python unittest¶
# python unittests only run the function with prefix "test"

>>> from __future__ import print_function
>>> import unittest
>>> class TestFoo(unittest.TestCase):
...     def test_foo(self):
...             self.assertTrue(True)
...     def fun_not_run(self):
...             print("no run")
...
>>> unittest.main()
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
>>> import unittest
>>> class TestFail(unittest.TestCase):
...     def test_false(self):
...             self.assertTrue(False)
...
>>> unittest.main()
F
======================================================================
FAIL: test_false (__main__.TestFail)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 3, in test_false
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)


Python unittest setup & teardown hierarchy
from __future__ import print_function

import unittest

def fib(n):
    return 1 if n<=2 else fib(n-1)+fib(n-2)

def setUpModule():
        print("setup module")
def tearDownModule():
        print("teardown module")

class TestFib(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.n = 10
    def tearDown(self):
        print("tearDown")
        del self.n
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def test_fib_assert_equal(self):
        self.assertEqual(fib(self.n), 55)
    def test_fib_assert_true(self):
        self.assertTrue(fib(self.n) == 55)

if __name__ == "__main__":
    unittest.main()

output:
python test.py
setup module
setUpClass
setUp
tearDown
.setUp
tearDown
.tearDownClass
teardown module

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

Different module of setUp & tearDown hierarchy
# test_module.py
from __future__ import print_function

import unittest

class TestFoo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("foo setUpClass")
    @classmethod
    def tearDownClass(self):
        print("foo tearDownClass")
    def setUp(self):
        print("foo setUp")
    def tearDown(self):
        print("foo tearDown")
    def test_foo(self):
        self.assertTrue(True)

class TestBar(unittest.TestCase):
    def setUp(self):
        print("bar setUp")
    def tearDown(self):
        print("bar tearDown")
    def test_bar(self):
        self.assertTrue(True)

# test.py
from __future__ import print_function

from test_module import TestFoo
from test_module import TestBar
import test_module
import unittest

def setUpModule():
    print("setUpModule")

def tearDownModule():
    print("tearDownModule")


if __name__ == "__main__":
    test_module.setUpModule = setUpModule
    test_module.tearDownModule = tearDownModule
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestBar)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner().run(suite)
output:
python test.py
setUpModule
foo setUpClass
foo setUp
foo tearDown
.foo tearDownClass
bar setUp
bar tearDown
.tearDownModule

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

Run tests via unittest.TextTestRunner¶
>>> import unittest

class TestRaiseException(unittest.TestCase):
    def test_raise_except(self):
        with self.assertRaises(SystemError):
            raise SystemError
suite_loader = unittest.TestLoader()
suite = suite_loader.loadTestsFromTestCase(TestRaiseException)
unittest.TextTestRunner().run(suite)
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
class TestRaiseFail(unittest.TestCase):
    def test_raise_fail(self):
        with self.assertRaises(SystemError):
            pass
suite = unittest.TestLoader().loadTestsFromTestCase(TestRaiseFail)
unittest.TextTestRunner(verbosity=2).run(suite)
test_raise_fail (__main__.TestRaiseFail) ... FAIL

======================================================================
FAIL: test_raise_fail (__main__.TestRaiseFail)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 4, in test_raise_fail
AssertionError: SystemError not raised

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
