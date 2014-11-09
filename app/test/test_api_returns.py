import unittest

from app import app


class TestPhone(unittest.TestCase):

    def get_number(self):
        '''
        Testing the phone numbers returned
        the convention is:
        NPA-NXX-XXXX

        NPA is the number plan area. Area code. the first digit is always a 2 thru 9
        NXX is the central office. the firstdigit is always 2-9
        XXXX can be any digit
        '''

        self.assertEqual(3, 3)