from flask import jsonify, request
from .model import Product
from . import db

def init_routes(app):
    @app.route('/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        products_list = [{
            'product_id': product.product_id,
            'product_name': product.product_name,
            'description': product.description,
            'price': str(product.price)
        } for product in products]
        return jsonify(products_list)

    @app.route('/products', methods=['POST'])
    def add_product():
        if request.is_json:
            data = request.get_json()
            # Check for duplicate product
            existing_product = Product.query.filter_by(product_name=data['product_name']).first()
            if existing_product:
                return jsonify({'error': 'Product already exists'}), 400
            
            new_product = Product(
                product_name=data['product_name'],
                description=data.get('description', ''),
                price=data['price']
            )
            db.session.add(new_product)
            db.session.commit()
            return jsonify({'message': 'Product added successfully'}), 201
        else:
            return jsonify({'error': 'Unsupported Media Type'}), 415
