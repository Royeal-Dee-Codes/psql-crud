from flask import Flask
from db import create_tables

from routes.products_routes import products
from routes.categories_routes import categories
from routes.companies_routes import companies
from routes.warranties_routes import warranties


app = Flask(__name__)


create_tables()

app.register_blueprint(products)
app.register_blueprint(categories)
app.register_blueprint(companies)
app.register_blueprint(warranties)


# @app.route('/companies', methods=['POST'])
# def create_company():
#     data = request.get_json()
#     company_id = str(uuid.uuid4())
#     cursor.execute("INSERT INTO Companies (company_id, company_name) VALUES (%s, %s)", (company_id, data['company_name']))
#     conn.commit()
#     response = jsonify({'message': 'Company created successfully', 'company_id': company_id})
#     return (response)


# @app.route('/categories', methods=['POST'])
# def create_category():
#     data = request.get_json()
#     category_id = str(uuid.uuid4())
#     cursor.execute("INSERT INTO Categories (category_id, category_name) VALUES (%s, %s)", (category_id, data['category_name']))
#     conn.commit()
#     response = jsonify({'message': 'Category created successfully', 'category_id': category_id})
#     return (response)


# @app.route('/products', methods=['POST'])
# def create_product():
#     data = request.get_json()
#     product_id = str(uuid.uuid4())
#     cursor.execute("INSERT INTO Products (product_id, company_id, company_name, price, description, active) VALUES (%s, %s, %s, %s, %s, %s)",
#                    (product_id, data['company_id'], data['company_name'], data['price'], data['description'], data['active']))
#     conn.commit()
#     response = jsonify({'message': 'Product created successfully', 'product_id': product_id})
#     return (response)


# @app.route('/warranties', methods=['POST'])
# def create_warranty():
#     data = request.get_json()
#     warranty_id = str(uuid.uuid4())
#     cursor.execute("INSERT INTO Warranties (warranty_id, product_id, warranty_months) VALUES (%s, %s, %s)",
#                    (warranty_id, data['product_id'], data['warranty_months']))
#     conn.commit()
#     response = jsonify({'message': 'Warranty created successfully', 'warranty_id': warranty_id})
#     return (response)


# @app.route('/companies', methods=['GET'])
# def get_companies():
#     cursor.execute("SELECT * FROM Companies")
#     rows = cursor.fetchall()
#     companies = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
#     response = jsonify(companies)
#     return (response)


# @app.route('/categories', methods=['GET'])
# def get_categories():
#     cursor.execute("SELECT * FROM Categories")
#     rows = cursor.fetchall()
#     categories = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
#     response = jsonify(categories)
#     return (response)


# @app.route('/products', methods=['GET'])
# def get_products():
#     cursor.execute("SELECT * FROM Products")
#     rows = cursor.fetchall()
#     products = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
#     response = jsonify(products)
#     return (response)


# @app.route('/warranties', methods=['GET'])
# def get_warranties():
#     cursor.execute("SELECT * FROM Warranties")
#     rows = cursor.fetchall()
#     warranties = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
#     response = jsonify(warranties)
#     return (response)


# @app.route('/products/active', methods=['GET'])
# def get_active_products():
#     cursor.execute("SELECT * FROM Products WHERE active = TRUE")
#     rows = cursor.fetchall()
#     active_products = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
#     response = jsonify(active_products)
#     return (response)


# @app.route('/products/company/<company_id>', methods=['GET'])
# def get_products_by_company(company_id):
#     cursor.execute("SELECT * FROM Products WHERE company_id = %s", (company_id,))
#     rows = cursor.fetchall()
#     products = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
#     response = jsonify(products)
#     return (response)


# @app.route('/companies/<company_id>', methods=['GET'])
# def get_company_by_id(company_id):
#     cursor.execute("SELECT * FROM Companies WHERE company_id = %s", (company_id,))
#     row = cursor.fetchone()
#     company = dict(zip([desc[0] for desc in cursor.description], row))
#     response = jsonify(company)
#     return (response)


# @app.route('/categories/<category_id>', methods=['GET'])
# def get_category_by_id(category_id):
#     cursor.execute("SELECT * FROM Categories WHERE category_id = %s", (category_id,))
#     category_row = cursor.fetchone()
#     category = dict(zip([desc[0] for desc in cursor.description], category_row))

#     cursor.execute("""
#         SELECT p.* FROM Products p
#         JOIN ProductsCategoriesXref pcx ON p.product_id = pcx.product_id
#         WHERE pcx.category_id = %s
#     """, (category_id,))
#     rows = cursor.fetchall()
#     products = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]

#     response = jsonify({'category': category, 'products': products})
#     return (response)


# @app.route('/products/<product_id>', methods=['GET'])
# def get_product_by_id(product_id):
#     cursor.execute("SELECT * FROM Products WHERE product_id = %s", (product_id,))
#     product_row = cursor.fetchone()
#     product = dict(zip([desc[0] for desc in cursor.description], product_row))

#     cursor.execute("SELECT * FROM Warranties WHERE product_id = %s", (product_id,))
#     warranty_row = cursor.fetchone()
#     warranty = dict(zip([desc[0] for desc in cursor.description], warranty_row))

#     cursor.execute("""
#         SELECT c.* FROM Categories c
#         JOIN ProductsCategoriesXref pcx ON c.category_id = pcx.category_id
#         WHERE pcx.product_id = %s
#     """, (product_id,))
#     rows = cursor.fetchall()
#     categories = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]

#     response = jsonify({'product': product, 'warranty': warranty, 'categories': categories})
#     return (response)


# @app.route('/warranties/<warranty_id>', methods=['GET'])
# def get_warranty_by_id(warranty_id):
#     cursor.execute("SELECT * FROM Warranties WHERE warranty_id = %s", (warranty_id,))
#     row = cursor.fetchone()
#     warranty = dict(zip([desc[0] for desc in cursor.description], row))
#     response = jsonify(warranty)
#     return (response)


# @app.route('/companies/<company_id>', methods=['PUT'])
# def update_company(company_id):
#     data = request.get_json()
#     cursor.execute("UPDATE Companies SET company_name = %s WHERE company_id = %s", (data['company_name'], company_id))
#     conn.commit()
#     response = jsonify({'message': 'Company updated successfully'})
#     return (response)


# @app.route('/categories/<category_id>', methods=['PUT'])
# def update_category(category_id):
#     data = request.get_json()
#     cursor.execute("UPDATE Categories SET category_name = %s WHERE category_id = %s", (data['category_name'], category_id))
#     conn.commit()
#     response = jsonify({'message': 'Category updated successfully'})
#     return (response)


# @app.route('/products/<product_id>', methods=['PUT'])
# def update_product(product_id):
#     data = request.get_json()
#     cursor.execute("UPDATE Products SET price = %s, description = %s, active = %s WHERE product_id = %s",
#                    (data['price'], data['description'], data['active'], product_id))
#     conn.commit()
#     response = jsonify({'message': 'Product updated successfully'})
#     return (response)


# @app.route('/warranties/<warranty_id>', methods=['PUT'])
# def update_warranty(warranty_id):
#     data = request.get_json()
#     cursor.execute("UPDATE Warranties SET warranty_months = %s WHERE warranty_id = %s",
#                    (data['warranty_months'], warranty_id))
#     conn.commit()
#     response = jsonify({'message': 'Warranty updated successfully'})
#     return (response)


# @app.route('/products/<product_id>', methods=['DELETE'])
# def delete_product(product_id):
#     cursor.execute("DELETE FROM Warranties WHERE product_id = %s", (product_id,))
#     cursor.execute("DELETE FROM ProductsCategoriesXref WHERE product_id = %s", (product_id,))
#     cursor.execute("DELETE FROM Products WHERE product_id = %s", (product_id,))
#     conn.commit()
#     response = jsonify({'message': 'Product and associated records deleted successfully'})
#     return (response)


# @app.route('/categories/<category_id>', methods=['DELETE'])
# def delete_category(category_id):
#     cursor.execute("DELETE FROM ProductsCategoriesXref WHERE category_id = %s", (category_id,))
#     cursor.execute("DELETE FROM Categories WHERE category_id = %s", (category_id,))
#     conn.commit()
#     response = jsonify({'message': 'Category and associated records deleted successfully'})
#     return (response)


# @app.route('/companies/<company_id>', methods=['DELETE'])
# def delete_company(company_id):
#     cursor.execute("DELETE FROM ProductsCategoriesXref WHERE product_id IN (SELECT product_id FROM Products WHERE company_id = %s)", (company_id,))
#     cursor.execute("DELETE FROM Warranties WHERE product_id IN (SELECT product_id FROM Products WHERE company_id = %s)", (company_id,))
#     cursor.execute("DELETE FROM Products WHERE company_id = %s", (company_id,))
#     cursor.execute("DELETE FROM Companies WHERE company_id = %s", (company_id,))
#     conn.commit()
#     response = jsonify({'message': 'Company and associated records deleted successfully'})
#     return (response)


# @app.route('/warranties/<warranty_id>', methods=['DELETE'])
# def delete_warranty(warranty_id):
#     cursor.execute("DELETE FROM Warranties WHERE warranty_id = %s", (warranty_id,))
#     conn.commit()
#     response = jsonify({'message': 'Warranty deleted successfully'})
#     return (response)


if __name__ == '__main__':
    app.run(debug=True)
