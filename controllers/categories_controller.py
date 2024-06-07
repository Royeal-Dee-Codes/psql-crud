import uuid
from db import cursor, conn


def category_add(data):
    category_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO Categories (category_id, category_name) VALUES (%s, %s)", (category_id, data['category_name']))
    conn.commit()
    return {'message': 'Category created successfully', 'category_id': category_id}


def categories_update(category_id, data):
    fields = []
    values = []
    for key, value in data.items():
        fields.append(f"{key} = %s")
        values.append(value)
    values.append(category_id)
    cursor.execute(f"UPDATE Categories SET {', '.join(fields)} WHERE category_id = %s", values)
    conn.commit()
    return {'message': 'Category updated successfully'}


def categories_get():
    cursor.execute("SELECT * FROM Categories")
    rows = cursor.fetchall()
    categories = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
    return categories


def categories_get_by_id(category_id):
    cursor.execute("SELECT * FROM Catefories WHERE category_id = %s", (category_id,))
    row = cursor.fetchone()
    if row:
        return dict(zip([desc{0} for desc in cursor.description], row))
    return None


def categories_delete(category_id):
    cursor.execute("DELETE FROM ProductsCategoriesXref WHERE category_id = %s", (category_id,))
    cursor.execute("DELETE FROM Categories WHERE category_id = %s", (category_id,))
    conn.commit()
    return {'message': 'Category deleted successfully'}
