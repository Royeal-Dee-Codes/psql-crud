import os
import psycopg2
from flask import jsonify


database = os.environ.get('DATABASE_NAME')
conn = psycopg2.connect(f'dbname={database}')
cursor = conn.cursor()


def company_add(request):
    post_data = request.form if request.form else request.json
    company_name = post_data['company_name']

    cursor.execute(
        """
            SELECT * FROM Companies
            WHERE company_name=%s;
        """,
        [company_name]
    )
    result = cursor.fetchone()

    if result:
        return jsonify({"message": "company already exists"}), 400

    if result == None:
        cursor.execute(
            """
                INSERT INTO Companies
                (company_name)
                VALUES(%s);
            """,
            [company_name]
        )
        conn.commit()

        cursor.execute(
            """
            SELECT * FROM Companies
            WHERE company_name=%s
        """,
            [company_name]
        )
        result = cursor.fetchone()

        if result:
            company_list = []

            company_record = {
                'company_id': result[0],
                'company_name': result[1]
            }

            company_list.append(company_record)

        return jsonify({"message": "company added", "results": company_list}), 201

    return jsonify({"message": "company cannot be added"}), 400


def companies_get():
    cursor.execute(
        """
            SELECT * 
            FROM Companies
        """
    )
    results = cursor.fetchall()

    if results:
        company_list = []

        for result in results:
            company_record = {
                'company_id': result[0],
                'company_name': result[1]
            }

            company_list.append(company_record)

        return jsonify({"message": "companies found", "results": company_list}), 200

    return jsonify({"message": "could not find data"}), 404


def company_get_by_id(request, company_id):
    post_data = request.form if request.form else request.json
    company_id = post_data['company_id']

    cursor.execute(
        """
            SELECT * 
            FROM Companies
            WHERE company_id=%s
        """
        [company_id]
    )
    results = cursor.fetchone()

    if results:
        company_list = []

        for result in results:
            company_record = {
                'company_id': result[0],
                'company_name': result[1]
            }

            company_list.append(company_record)

        return jsonify({"message": "companies found", "results": company_list}), 200

    return jsonify({"message": "could not find data"}), 404


def company_update(request, company_id):
    post_data = request.form if request.form else request.json
    company_name = post_data['company_name']

    cursor.execute(
        """
            SELECT * FROM Companies
            WHERE company_id=%s
        """,
        [company_id]
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
                UPDATE Companies
                SET company_name=%s
                WHERE company_id=%s;
            """,
            [company_name, company_id]
        )
        conn.commit()

        cursor.execute(
            """
            SELECT * FROM Companies
            WHERE company_id=%s
        """,
            [company_id]
        )
        company = cursor.fetchone()

        company_list = []

        company_record = {
            'company_id': company[0],
            'company_name': company[1]
        }

        company_list.append(company_record)

        return jsonify({"message": "company updated", "results": company_list}), 200

    return jsonify({"message": "company not found"}), 404


def company_delete(company_id):
    company = {}
    company['company_id'] = int(company_id)

    if not company['company_id']:
        return jsonify({"message": "company not found"}), 404

    cursor.execute(
        """
            SELECT * FROM Companies
            WHERE company_id=%s
        """,
        [company_id]
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
                DELETE FROM Companies
                WHERE company_id=%s
            """,
            [company_id]
        )
        conn.commit()

        return jsonify({"message": "company deleted"}), 200

    return jsonify({"message": "could not delete company"}), 400
