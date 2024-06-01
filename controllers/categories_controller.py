import uuid
from db import cursor, conn


def create_category(data):
    category_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO Categories (category_id, category_name) VALUES (%s, %s)", (category_id, data['category_name']))
    conn.commit()
    return {'message': 'Category created successfully', 'category_id': category_id}


def get_categories():
    cursor.execute("SELECT * FROM Categories")
    rows = cursor.fetchall()
    categories = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
    return categories
