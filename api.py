# api.py

from flask import request, jsonify
from flask_restful import Resource
from app.models import Product, db

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([product.serialize() for product in products])

    def post(self):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        if not all([name, description, price]):
            return {'message': 'Missing required data'}, 400

        product = Product(name=name, description=description, price=price)
        db.session.add(product)
        db.session.commit()

        return jsonify(product.serialize()), 201
