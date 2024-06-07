from flask import Blueprint, request
import controllers
import controllers.companies_controller

companies = Blueprint('companies', __name__)


@companies.route('/companies', methods=['POST'])
def company_add():
    return controllers.company_add(request)


@companies.route('/companies/<companies_id>', methods=['PUT'])
def companies_update(company_id):
    return controllers.companies_update(request, company_id)


@companies.route('/companies', methods=["GET"])
def companies_get():
    return controllers.companies_get(request)


@companies.route('/companies/<category_id>', methods=['GET'])
def companies_get_by_id(company_id):
    return controllers.companies_get_by_id(request, company_id)


@companies.route('/companies/delete/<category_id>', methods=['DELETE'])
def companies_delete(company_id):
    return controllers.companies_controller(request, company_id)


@companies.route('/companies/status/<company_id>', methods=['PATCH'])
def companies_activity(company_id):
    return controllers.companies_controller(request, company_id)
