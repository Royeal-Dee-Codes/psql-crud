import uuid
from db import cursor, conn


def create_product(data):
    product_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO Products (product_id, company_id, company_name, price, description, active) VALUES (%s, %s, %s, %s, %s, %s)", (product_id, data['company_id'], data['company_name'], data['price'], data['descripton'], data['active']))
    conn.commit()
    return {'message': 'Product created successfully', 'product_id': product_id}


def get_products():
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    products = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
    return products
