import program
import unittest


class TestProgram(unittest.TestCase):
    def setUp(self):
        """Init"""
    def Test_program(self):
        self.assertTrue(program.set_password('bAse730onE'))
        self.assertFalse(program.set_password('A1213pokl'))

    def tearDown(self):
        """Finish"""
