import psycopg2
import uuid
from datetime import date


def create_connection():
    return psycopg2.connect(
        host='college-crud-instance-1.csaohqjx3mfa.us-east-1.rds.amazonaws.com',
        database='postgres',
        user='postgres',
        password='12345678',
        port='5432'
    )


def get_all_users():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('select *, name from users')
    rows = cursor.fetchall()
    users = []

    for row in rows:
        user = (f'id: {row[0]}', f'name: {row[1]}', f'email: {row[2]}',
                f'password: {row[3]}', f'created_at: {row[4]}', f'updated_at: {row[5]}')
        users.append(user)

    cursor.close()
    connection.close()

    return users


def get_user_by_id(user_id):
    connection = create_connection()
    cursor = connection.cursor()
    user_id = "'{0}'".format(user_id)
    cursor.execute('SELECT id, name, email, password FROM users WHERE id = {0}'.format(
        user_id))
    user_data = cursor.fetchone()
    user = (
        'user: {0}'.format(user_data[0]),
        'name: {0}'.format(user_data[1]),
        'email: {0}'.format(user_data[2]),
        'password: {0}'.format(user_data[3]))

    cursor.close()
    connection.close()

    return user


def create_user(name, email, password):
    connection = create_connection()
    cursor = connection.cursor()
    user_id = uuid.uuid1()
    user = (name, email, password)

    cursor.execute("INSERT INTO users(id, name, email, password, created_at, updated_at) VALUES(%s, %s, %s, %s, %s, %s)",
                   (str(user_id), name, email, password, '2017-03-18 00:00:00', '2017-03-18 00:00:00'))

    connection.commit()
    cursor.close()
    connection.close()
    return user
