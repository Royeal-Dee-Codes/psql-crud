from flask import Blueprint, request
import controllers

categories = Blueprint('categories', __name__)


@categories.route('/categories', methods=['POST'])
def category_add():
    return controllers.category_add(request)


@categories.route('/categories/<category_id>', methods=['PUT'])
def categories_update(category_id):
    return controllers.category_update(request, category_id)


@categories.route('/categories', methods=['GET'])
def categories_get():
    return controllers.category_get(request)


@categories.route('/categories/<category_id>', methods=['GET'])
def categories_get_by_id(category_id):
    return controllers.categories_get_by_id(request, category_id)


@categories.route('/categories/delete/<category_id>', methods=['DELETE'])
def categories_delete(category_id):
    return controllers.categories_delete(request, category_id)


@categories.route('/categories/status/<category_id>', methods=['PATCH'])
def categories_activity(category_id):
    return controllers.categories_activity(request, category_id)
