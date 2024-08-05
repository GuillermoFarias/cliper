""" Api Controller Test"""
from core.testing.test_case import TestCase
from core.facades.app import App

class TestApiController(TestCase):
    """ ApiController test class """

    def test_example1(self):
        """ Test example 1 """
        print("Running test_example1")
        assert 1 + 1 == 2

    def test_example2(self):
        """ Test example 2 """
        print("Running test_example2")
        assert 1 + 2 == 3

    def test_example3(self):
        """ Test example 3 """
        print("Running test_example3")
        assert "hello".upper() == "HELLO"
