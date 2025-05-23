import psycopg2
from flask import current_app

def get_db_connection():
    conn = psycopg2.connect(
        dbname=current_app.config['DB_NAME'],
        user=current_app.config['DB_USER'],
        password=current_app.config['DB_PASSWORD'],
        host=current_app.config['DB_HOST'],
        port=current_app.config['DB_PORT']
    )
    return conn

def get_all_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

def get_or_create_user_by_google_id(google_id, email, name, picture):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE google_id = %s", (google_id,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
    else:
        cur.execute(
            "INSERT INTO users (google_id, email, name, profile_pic) VALUES (%s, %s, %s, %s) RETURNING id",
            (google_id, email, name, picture)
        )
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id