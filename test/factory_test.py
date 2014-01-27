import goldkeys
import unittest
import json

class FactoryTestCase(unittest.TestCase):
    def setUp(self):
        goldkeys.app.config['TESTING'] = True
        self.app = goldkeys.app.test_client()

    def testFactoryDataExists(self):
        response = self.app.get('/factory')
        self.assertIsNotNone(response.data)

    def testFirstFactoryIsCorrect(self):
        response = self.app.get('/factory')
        json_data = json.loads(response.data)[0]
        self.assertEqual(json_data['nickname'], 'Maphar')

if __name__ == '__main__':
    unittest.main()
