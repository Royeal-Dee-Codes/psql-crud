import os
from flask import Flask
import psycopg2

from db import create_tables

import routes


database = os.environ.get('DATABASE_NAME')
app_host = os.environ.get('APP_HOST')
app_port = os.environ.get('APP_PORT')

conn = psycopg2.connect(f"dbname={database}")
cursor = conn.cursor()

app = Flask(__name__)


app.register_blueprint(routes.products)
app.register_blueprint(routes.categories)
app.register_blueprint(routes.companies)
app.register_blueprint(routes.warranties)


if __name__ == '__main__':
    create_tables(conn, cursor)
    app.run(host=app_host, port=app_port, debug=True)
