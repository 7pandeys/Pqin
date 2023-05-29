import unittest
import json
from flask import Flask
from flask.testing import FlaskClient
from app import app

class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_random_array_endpoint(self):
        # Prepare the request payload
        payload = {
            'sentence': 'This is an example sentence'
        }

        # Send a POST request to the API endpoint
        response = self.app.post('/api/random_array', json=payload)

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the response content type is JSON
        self.assertEqual(response.content_type, 'application/json')

        # Parse the response JSON data
        response_data = json.loads(response.data)

        # Assert the response data is a list
        self.assertIsInstance(response_data, list)

        # Assert the response data has 500 elements
        self.assertEqual(len(response_data), 500)

        # Assert each element in the response data is a float
        for element in response_data:
            self.assertIsInstance(element, float)

if __name__ == '__main__':
    unittest.main()
