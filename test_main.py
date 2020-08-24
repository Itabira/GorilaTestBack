import unittest

from main import app

class FlaskTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/investments")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/investments")
        self.assertEqual(response.content_type,"application/json")
    
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/investments")
        self.assertTrue(b'investments' in response.data)
    


if __name__ == "__main__":
    unittest.main()