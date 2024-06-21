import os
import psycopg2
from flask import jsonify


database = os.environ.get('DATABASE_NAME')
conn = psycopg2. connect(f'dbname={database}')
cursor = conn.cursor()


# add
def product_add(request):
    post_data = request.form if request.form else request.json
    product_id = post_data['product_id']

    cursor.execute(
        """
            SELECT * FROM Products
            WHERE product_id=%s;
        """, [product_id]
    )
    result = cursor.fetchone()

    if result:
        return jsonify({"message": "product already exists"}), 400

    if result == None:
        cursor.execute(
            """
                INSERT INTO Products
                (product_id)
                VALUES(%s)
            """, [product_id]
        )
        conn.commit()

        cursor.execute(
            """
                SELECT * FROM Products
                WHERE product_id=%s
            """, [product_id]
        )
        result = cursor.fetchone()

        if result:
            product_list = []

            product_record = {
                'product_id': result[0],
                'company_id': result[1],
                'company_name': result[2],
                'price': result[3],
                'description': result[4],
                'active': result[5]
            }

            product_list.append(product_record)

        return jsonify({"message": "product added", "results": product_list}), 201

    return jsonify({"message": "product cannot be added"}), 400


# get
def product_get():
    cursor.execute(
        """
            SELECT *
            FROM Products
        """
    )
    results = cursor.fetchall()

    if results:
        product_list = []

        for result in results:
            product_record = {
                'product_id': result[0],
                'company_id': result[1],
                'company_name': result[2],
                'price': result[3],
                'description': result[4],
                'active': result[5]
            }

            product_list.append(product_record)

        return jsonify({"message": "products found", "result": product_list}), 200

    return jsonify({"message": "could not find data"}), 404


# get
def products_get():
    cursor.execute(
        """
            SELECT *
            FROM Products
        """
    )
    results = cursor.fetchall()

    if results:
        product_list = []

        for result in results:
            product_record = {
                'product_id': result[0],
                'company_id': result[1],
                'company_name': result[2],
                'price': result[3],
                'description': result[4],
                'active': result[5]
            }

            product_list.append(product_record)

        return jsonify({"message": "products found", "results": product_list}), 200

    return jsonify({"message": "could not find data"}), 404


# get_by_id
def product_get_by_id(request, product_id):
    post_data = request.form if request.form else request.json
    product_id = post_data['product_id']

    cursor.execute(
        """
            SELECT *
            FROM Products
            WHERE product=%s
        """ [product_id]
    )
    results = cursor.fetchone()

    if results:
        product_list = []

        for result in results:
            product_record = {
                'product_id': result[0],
                'company_id': result[1],
                'company_name': result[2],
                'price': result[3],
                'description': result[4],
                'active': result[5]
            }

            product_list.append(product_record)

        return jsonify({"message": "products found", "results": product_list}), 200

    return jsonify({"message": "could not find data"}), 404


# update
def product_update(request, product_id):
    post_data = request.form if request.form else request.jsonify
    product_id = post_data['product_id']

    cursor.execute(
        """
            SELECT * FROM Products
            WHERE product_id%s
        """, [product_id]
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
                UPDATE Products
                SET product_id=%s
                WHERE product_id=%s
            """, [product_id]
        )
        conn.commit()

        cursor.execute(
            """
                SELECT * FROM Products
                WHERE product_id=%s
            """, [product_id]
        )
        product = cursor.fetchone()

        product_list = []

        product_record = {
            'product_id': result[0],
            'company_name': result[1],
            'company_name': result[2],
            'price': result[3],
            'description': result[4],
            'active': result[5]
        }

        product_list.append(product_record)

        return jsonify({"message": "product updated", "results": product_list}), 200

    return jsonify({"message": "product not found"}), 404


# delete
def product_delete(product_id):
    product = {}
    product['product_id'] = int(product_id)

    if not product['product_id']:
        return jsonify({"message": "product not found"}), 404

    cursor.execute(
        """
            SELECT * FROM Products
            WHERE product_id=%s
        """, [product_id]
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
                DELETE FROM Products
                WHERE product_id=%s
            """, [product_id]
        )
        conn.commit()

        return jsonify({"message": "product deleted"}), 200

    return jsonify({"message": "could not delete product"}), 400


# activity
def product_activity(product_id, active_status):
    cursor.execute(
        """
            UPDATE Products
            SET active=%s
            WHERE product_id=%s;
        """, [active_status, product_id]
    )
    conn.commit()
    return jsonify({"message": f"product with product_id {product_id} set to {active_status}"}), 200
