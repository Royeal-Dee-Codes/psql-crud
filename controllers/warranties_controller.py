import uuid
from db import cursor, conn


def create_warranty(data):
    warranty_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO Warranties (warranty_id, product_id, warranty_months) VALUES (%s, %s, %s)", (warranty_id, data['product_id'], data['warranty_months']))
    conn.commit()
    return {'message': 'Warranty created successfully', 'warranty_id': warranty_id}


def get_warranties():
    cursor.execute("SELECT * FROM Warranties")
    rows = cursor.fetchall()
    warranties = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
    return warranties
