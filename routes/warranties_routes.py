from flask import Blueprint, request
import controllers

warranties = Blueprint('warranties', __name__)


@warranties.route('/warranties', methods=['POST'])
def warranty_add():
    return controllers.warranty_add(request)


@warranties.route('/warranties/<warranty_id>', methods=['PUT'])
def warranties_update(warranty_id):
    return controllers.warranties_update(request, warranty_id)


@warranties.route('/warranties', methods=['GET'])
def get_warranties():
    return controllers.get_warranties(request)


@warranties.route('/warranties/<warranty_id>', methods=['GET'])
def warranties_get_by_id(warranty_id):
    return controllers.warranties_get_by_id(request, warranty_id)


@warranties.route('/warranties/delete/<warranty_id>', methods=['DELETE'])
def warranties_delete(warranty_id):
    return controllers.warranties_delete(request, warranty_id)


@warranties.route('/warranties/status/<warranty_id>', methods=['PATCH'])
def warranties_activity(warranty_id):
    return controllers.warranties_activity(request, warranty_id)
