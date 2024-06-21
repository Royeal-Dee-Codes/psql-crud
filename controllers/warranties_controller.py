import os
import psycopg2
from flask import jsonify

database = os.environ.get('DATABASE_NAME')
conn = psycopg2.connect(f'dbname={database}')
cursor = conn.cursor()


# add
def warranty_add(request):
    post_data = request.form if request.form else request.json
    warranty_id = post_data['warranty_id']

    cursor.execute(
        """
            SELECT * FROM Warranties
            WHERE warranty_id=%s;
        """, [warranty_id]
    )
    result = cursor.fetchone()

    if result:
        return jsonify({"message": "warranty already exists"}), 400

    if result == None:
        cursor.execute(
            """
                INSERT INTO Warranties
                (warranty_id)
                VALUES(%s)
            """, [warranty_id]
        )
        conn.commit()

        cursor.execute(
            """
                SELECT * FROM Warranties
                WHERE warranty_id=%s
            """, [warranty_id]
        )
        result = cursor.fetchone()

        if result:
            warranty_list = []

            warranty_record = {
                'warranty_id': result[0]
            }

            warranty_list.append(warranty_record)

        return jsonify({"message": "warranty added", "results": warranty_list}), 201

    return jsonify({"message": "warranty cannot be added"}), 400


# get
def warranty_get():
    cursor.execute(
        """
            SELECT *
            FROM Warranties
        """
    )
    results = cursor.fetchall()

    if results:
        warranty_list = []

        for result in results:
            warranty_record = {
                'warranty_id': result[0],
                'product_id': result[1]
            }

            warranty_list.append(warranty_record)

        return jsonify({"message": "warranties found", "result": warranty_list}), 200

    return jsonify({"message": "could not find data"}), 404


# get
def warranties_get():
    cursor.execute(
        """
            SELECT * 
            FROM Warranties
        """
    )
    results = cursor.fetchall()

    if results:
        warranty_list = []

        for result in results:
            warranty_record = {
                'warranty_id': result[0],
                'product_id': result[1]
            }

            warranty_list.append(warranty_record)

        return jsonify({"message": "warranties found", "results": warranty_list}), 200

    return jsonify({"message": "could not find data"}), 404


# get_by_id
def warranty_get_by_id(request, warranty_id):
    post_data = request.form if request.form else request.json
    warranty_id = post_data['warranty_id']

    cursor.execute(
        """
            SELECT *
            FROM Companies
            WHERE warranty=%s
        """ [warranty_id]
    )
    results = cursor.fetchone()

    if results:
        warranty_list = []

        for result in results:
            warranty_record = {
                'warranty_id': result[0],
                'product_id': result[1]
            }

            warranty_list.append(warranty_record)

        return jsonify({"message": "warranties found", "results": warranty_list}), 200

    return jsonify({"message": "could not find data"}), 404


# update
def warranty_update(request, warranty_id):
    post_data = request.form if request.form else request.json
    warranty_id = post_data['warranty_id']

    cursor.execute(
        """
            SELECT * FROM Warranties
            WHERE warranty_id%s
        """, [warranty_id]
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
                UPDATE Warranties
                SET warranty_id=$
                WHERE warranty_id=%s;
            """, [warranty_id]
        )
        conn.commit()

        cursor.execute(
            """
                SELECT * FROM Warranties
                WHERE warranty_id=%s
            """, [warranty_id]
        )
        result = cursor.fetchone()

        warranty_list = []

        warranty_record = {
            'warranty_id': result[0],
            'product_id': result[1]
        }

        warranty_list.append(warranty_record)

        return jsonify({"message": "warranty updated", "results": warranty_list}), 200

    return jsonify({"message": "warranty not found"}), 404


# delete
def warranty_delete(warranty_id):
    warranty = {}
    warranty['warranty_id'] = int(warranty_id)

    if not warranty['warranty_id']:
        return jsonify({"message": "warranty not found"}), 404

    cursor.execute(
        """
            SELECT * FROM Warranties
            WHERE warranty_id=%s
        """, [warranty_id]
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
                DELETE FROM Warranties
                WHERE warranty_id=%s
            """, [warranty_id]
        )
        conn.commit()

        return jsonify({"message": "warranty deleted"}), 200

    return jsonify({"message": "could not delete warranty"}), 400


# activity
def warranty_activity(warranty_id, active_status):
    cursor.execute(
        """
            UPDATE Warranties
            SET active=%s
            WHERE warranty_id=%s;
        """, [active_status, warranty_id]
    )
    conn.commit()
    return jsonify({"message": f"warranty with warranty_id {warranty_id} set to {active_status}"}), 200
