import os
import psycopg2
from flask import jsonify

database = os.environ.get('DATABASE_NAME')
conn = psycopg2.connect(f'dbname={database}')
cursor = conn.cursor()


# add
def categories_add(request):
    post_data = request.form if request.form else request.json
    category_id = post_data['product_id']

    cursor.execute(
        """
            SELECT * FROM Categories
            WHERE category_id=%s;
        """, [category_id]
    )
    result = cursor.fetchone()

    if result:
        return jsonify({"message": "category already exists"}), 400

    if result == None:
        cursor.execute(
            """
                INSERT INTO Categories
                (category_id)
                VALUES(%s)
            """, [category_id]
        )
        conn.commit()

        cursor.execute(
            """
                INSERT INTO Categories
                (category_id)
                VALUES(%s)
            """, [category_id]
        )
        conn.commit()

        cursor.execute(
            """
                SELECT * FROM Categories
                WHERE category_id=%s
            """, [category_id]
        )
        result = cursor.fetchone()

        if result:
            category_list = []

            category_record = {
                'category_id': result[0],
                'category_name': result[1]
            }

            category_list.append(category_record)

        return jsonify({"message": "category added", "results": category_list}), 201

    return jsonify({"message": "category cannot be added"}), 400


# get
def category_get():
    cursor.execute(
        """
            SELECT * 
            FROM Categories
        """
    )
    results = cursor.fetchone()

    if results:
        category_list = []

        for result in results:
            category_record = {
                'category_id': result[0],
                'category_name': result[1]
            }

            category_list.append(category_record)

        return jsonify({"message": "categories found", "results": category_list}), 200

    return jsonify({"message": "could not find data"}), 404


# get_by_id
def category_get_by_id(request, category_id):
    post_data = request.form if request.form else request.json
    category_id = post_data['category_id']

    cursor.execute(
        """
            SELECT *
            FROM Categories
            WHERE category=%s
        """ [category_id]
    )
    results = cursor.fetchone()

    if results:
        category_list = []

        for result in results:
            category_record = {
                'category_id': result[0],
                'company_name': result[1]
            }

            category_list.append(category_record)

        return jsonify({"message": "categories found", "results": category_list}), 200

    return jsonify({"message": "could not find data"}), 404


# update
def category_update(request, category_id):
    post_data = request.form if request.form else request.json
    category_id = post_data['category_id']

    cursor.execute(
        """
            SELECt * FROM Categories
            WHERE category_id%s
        """, [category_id]
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
                UPDATE Categories
                SET category_id=%s
                WHERE category_id=%s;
            """, [category_id]
        )
        conn.commit()

        cursor.execute(
            """
                SELECT * FROM Categories
                WHERE category_id=%s
            """, [category_id]
        )
        result = cursor.fetchone()

        category_list = []

        category_record = {
            'category_id': result[0],
            'category_name': result[1]
        }

        category_list.append(category_record)

        return jsonify({"message": "category updated", "results": category_list}), 200

    return jsonify({"message": "category not found"}), 404


# delete
def category_delete(category_id):
    category = {}
    category['category_id'] = int(category_id)

    if not category['category_id']:
        return jsonify({"message": "category not found"}), 404

    cursor.execute(
        """
            SELECT * FROM Categories
            WHERE category_id=%s
        """, [category_id]
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
                DELETE FROM Categories
                WHERE category_id=%s
            """, [category_id]
        )
        conn.commit()

        return jsonify({"message": "category deleted"}), 200

    return jsonify({"message": "could not delete category"}), 400


# activity
def category_activity(category_id, active_status):
    cursor.execute(
        """
            UPDATE Categories
            SET active=%s
            WHERE category_id=%s;
        """, [active_status, category_id]
    )
    conn.commit()
    return jsonify({"message": f"category with category_id {category_id} set to {active_status}"}), 200
