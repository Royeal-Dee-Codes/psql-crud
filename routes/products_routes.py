from flask import Blueprint, request
import controllers

products = Blueprint('products', __name__)


@products.route('/products', methods=['POST'])
def product_add():
    return controllers.product_add(request)


@products.route('/products/<product_id>', methods=['PUT'])
def product_update(product_id):
    return controllers.product_update(request, product_id)


@products.route('/products', methods=['GET'])
def products_get(product_id):
    return controllers.products_get(request, product_id)


@products.route('/products/<product_id>', methods=['GET'])
def products_get_by_id(product_id):
    return controllers.products_get_by_id(request, product_id)


@products.route('/products/delete/<product_id>', methods=['DELETE'])
def products_delete(product_id):
    return controllers.products_delete(request, product_id)


@products.route('/products/status/<product_id>', methods=['PATCH'])
def products_activity(product_id):
    return controllers.products_activity(request, product_id)
