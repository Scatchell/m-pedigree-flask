import goldkeys
import unittest
import json

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        goldkeys.app.config['TESTING'] = True
        self.app = goldkeys.app.test_client()

    def testCompanyDataExists(self):
        response = self.app.get('/company')
        self.assertIsNotNone(response.data)

    def testFirstCompanyIsCorrect(self):
        response = self.app.get('/company/1')
        json_data = json.loads(response.data)
        self.assertEqual(json_data['company_code'], '123456')

if __name__ == '__main__':
    unittest.main()
