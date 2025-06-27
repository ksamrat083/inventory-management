from flask import Blueprint, request, jsonify
from app.models import db, Product, Category, Supplier

products_bp = Blueprint('products', __name__)

# GET all products
@products_bp.route('/products/', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = []
    for product in products:
        result.append({
            'id': product.id,
            'name': product.name,
            'stock': product.stock,
            'low_stock_threshold': product.low_stock_threshold,
            'category': product.category.name if product.category else None,
            'supplier': product.supplier.name if product.supplier else None
        })
    return jsonify(result), 200

# GET product by ID
@products_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'stock': product.stock,
        'low_stock_threshold': product.low_stock_threshold,
        'category': product.category.name if product.category else None,
        'supplier': product.supplier.name if product.supplier else None
    }), 200

# POST - create new product
@products_bp.route('/products/', methods=['POST'])
def create_product():
    data = request.get_json()

    if not data or not all(k in data for k in ('name', 'stock', 'low_stock_threshold', 'category_id', 'supplier_id')):
        return jsonify({'error': 'Missing required fields'}), 400

    product = Product(
        name=data['name'],
        stock=data['stock'],
        low_stock_threshold=data['low_stock_threshold'],
        category_id=data['category_id'],
        supplier_id=data['supplier_id']
    )
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Product created', 'id': product.id}), 201

# PUT - update product
@products_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()

    product.name = data.get('name', product.name)
    product.stock = data.get('stock', product.stock)
    product.low_stock_threshold = data.get('low_stock_threshold', product.low_stock_threshold)
    product.category_id = data.get('category_id', product.category_id)
    product.supplier_id = data.get('supplier_id', product.supplier_id)

    db.session.commit()
    return jsonify({'message': 'Product updated'}), 200

# DELETE - delete product
@products_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 200
