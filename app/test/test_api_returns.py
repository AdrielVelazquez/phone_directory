import unittest

from app import app

from app.tools.phone_numbers import get_random_start_n, get_area_code, get_phone_number
import utils_unittest



class TestPhone(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.from_object("app.test.config_test")
        if not app.config['PHONE_DB'].startswith("test"):
            print "YIKES THESE ARE NOT TEST DATABASES! EXITING!"
            exit()
        utils_unittest.setup_database(db_name=app.config['PHONE_DB'])

    @classmethod
    def tearDownClass(cls):
        print "ApiSigninTestCase: tear down"
        utils_unittest.tear_down_database(db_name=app.config['PHONE_DB'], delete=True)

    def test_get_number(self):
        '''
        Testing the phone numbers returned
        the convention is:
        NPA-NXX-XXXX

        NPA is the number plan area. Area code. the first digit is always a 2 thru 9
        NXX is the central office. the firstdigit is always 2-9
        XXXX can be any digit
        '''

        for i in range(1000):
            num = get_random_start_n()
            self.assertTrue(int(num) > 1)

    def test_area_code(self):
        '''
        Test that area code is greater than 199
        '''
        for i in range(1000):
            area = get_area_code()
            self.assertTrue(int(area) > 199)

    def test_unique_numbers(self):
        '''
        Test that a unique number is always generated
        '''
        numbers = set()
        for i in range(1000):
            numbers.add(get_phone_number(user="Adriel"))
        self.assertTrue(len(numbers) == 1000)

    def test_responses(self):
        '''
        Testing that all the responses are properly happening
        '''
        self.app = app.test_client()
        response = self.app.get('/SET/number', content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/SET/assigned', content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/SET/unassign', content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
