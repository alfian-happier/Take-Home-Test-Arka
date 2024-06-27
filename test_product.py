import unittest
from app import create_app, db
from app.model import Product

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        print("Setting up the test case...")
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

        with self.app.app_context():
            # db.drop_all()
            db.create_all()

    def tearDown(self):
         print("Tearing down the test case...")
         with self.app.app_context():
            db.session.remove()
            #db.drop_all()

    def test_add_product(self):
        print("Testing POST /products endpoint...")
        new_product = {
            'product_name': 'Gas',
            'description': 'Cruel Gas',
            'price': 70.00
        }
        
        response = self.client.post('/products', json=new_product)
        print(f"Response status code: {response.status_code}")
        print(f"Response JSON: {response.json}")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Product added successfully')

if __name__ == '__main__':
    unittest.main()
