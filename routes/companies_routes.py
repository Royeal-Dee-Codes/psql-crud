from flask import Blueprint, request

import controllers

companies = Blueprint('companies', __name__)


@companies.route('/company', methods=['POST'])
def company_add():
    return controllers.company_add(request)


@companies.route('/companies', methods=["GET"])
def companies_get():
    return controllers.companies_get()


@companies.route('/company/<company_id>', methods=['GET'])
def company_get_by_id(company_id):
    return controllers.company_get_by_id(request, company_id)


@companies.route('/company/<company_id>', methods=['PUT'])
def company_update(company_id):
    return controllers.company_update(request, company_id)


@companies.route('/company/delete/<company_id>', methods=['DELETE'])
def company_delete(company_id):
    return controllers.company_delete(company_id)


@companies.route('/companies/status/<company_id>', methods=['GET'])
def comapanies_get_by_activity(company_id):
    return controllers.companies_controller(request, company_id)


@companies.route('/companies/status/<company_id>', methods=['PATCH'])
def companies_activity(company_id):
    return controllers.companies_controller(request, company_id)
