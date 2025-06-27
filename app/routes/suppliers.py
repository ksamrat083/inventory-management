from flask import Blueprint, request, jsonify
from app.models import db, Supplier

suppliers_bp = Blueprint('suppliers', __name__, url_prefix='/suppliers')


# Serialize supplier
def serialize_supplier(supplier):
    return {
        "id": supplier.id,
        "name": supplier.name,
        "contact_info": supplier.contact_info
    }


# GET /suppliers/
@suppliers_bp.route('/', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([serialize_supplier(s) for s in suppliers])


# GET /suppliers/<int:id>
@suppliers_bp.route('/<int:id>', methods=['GET'])
def get_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    return jsonify(serialize_supplier(supplier))


# POST /suppliers/
@suppliers_bp.route('/', methods=['POST'])
def create_supplier():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    supplier = Supplier(
        name=data['name'],
        contact_info=data.get('contact_info', '')
    )
    db.session.add(supplier)
    db.session.commit()
    return jsonify(serialize_supplier(supplier)), 201


# PUT /suppliers/<int:id>
@suppliers_bp.route('/<int:id>', methods=['PUT'])
def update_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    data = request.get_json()
    supplier.name = data.get('name', supplier.name)
    supplier.contact_info = data.get('contact_info', supplier.contact_info)
    db.session.commit()
    return jsonify(serialize_supplier(supplier))


# DELETE /suppliers/<int:id>
@suppliers_bp.route('/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    db.session.delete(supplier)
    db.session.commit()
    return jsonify({"message": "Supplier deleted successfully"})
