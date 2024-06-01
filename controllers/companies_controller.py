import uuid
from db import cursor, conn


def create_company(data):
    company_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO Companies (company_id, company_name) VALUES (%s, %s)", (company_id, data['company_name']))
    conn.commit()
    return {'message': 'Company created successfully', 'company_id': company_id}


def get_companies():
    cursor.execute("SELECT * FROM Companies")
    rows = cursor.fetchall()
    companies = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
    return companies
