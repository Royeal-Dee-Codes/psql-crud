import os
import psycopg2

DATABASE_NAME = os.environ.get("DATABASE_NAME")

conn = psycopg2.connect(f"dbname={DATABASE_NAME}")
cursor = conn.cursor()


def create_tables():
    print("Creating tables...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Companies (
            company_id UUID PRIMARY KEY,
            company_name VARCHAR NOT NULL UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categories (
            category_id UUID PRIMARY KEY,
            category_name VARCHAR NOT NULL UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
        product_id UUID PRIMARY KEY,
        company_id UUID REFERENCES Companies(company_id),
        company_name VARCHAR NOT NULL UNIQUE,
        price INTEGER,
        description VARCHAR,
        active BOOLEAN DEFAULT true
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Warranties (
            warranty_id UUID PRIMARY KEY,
            product_id UUID REFERENCES Products(product_id),
            warranty_months VARCHAR NOT NULL
        );
    """)
    conn.commit()
    print("Tables created")
