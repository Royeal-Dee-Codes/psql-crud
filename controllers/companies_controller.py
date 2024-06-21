import os
import psycopg2
from flask import jsonify


database = os.environ.get('DATABASE_NAME')
conn = psycopg2.connect(f'dbname={database}')
cursor = conn.cursor()


# add
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


# get
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


# get_by_id
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


# update
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


# delete
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


# get_by_activity
def companies_get_by_activity(active_status):
    cursor.execute(
        """
            SELECT * FROM Companies
            WHERE active=%s;
        """, [active_status]
    )
    results = cursor.fetchall()

    if results:
        company_list = []
        for company in results:
            company_record = {
                'company_id': company[0],
                'company_name': company[1],
                'active': company[2]
            }
            company_list.append(company_record)
        return jsonify({"message": "company found", "results": company_list}), 200
    else:
        print({"message": f"no company found with the active status set to {active_status}"}), 404


# activity
def company_acivity(company_id, active_status):
    cursor.execute(
        """
            UPDATE Companies
            SET active=%s
            WHERE company_id=%s;
        """, [active_status, company_id]
    )
    conn.commit()
    return jsonify({"message": f"company with company_id {company_id} set to {active_status}"}), 200
