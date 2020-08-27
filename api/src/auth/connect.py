import pymysql as db
from flask import current_app, jsonify

DEFAULT_PORT = 3306


def execute(query):
    """
    This function opens a connection to the database,
    executes and commits a supplied query.
    :param query: string SQL syntax
    :return: Results of the query.
    """
    try:
        config = current_app.config
        conn = db.connect(user=config['MYSQL_USER'],
                          password=config['MYSQL_PASSWORD'],
                          host=config['MYSQL_HOST'],
                          port=int(config['MYSQL_PORT']),
                          database=config['MYSQL_DATABASE'])
        cur = conn.cursor()
        cur.execute(query)
        rv = cur.fetchall()
        return jsonify(rv)
    except db.Error as e:
        print(f"Error: {e}")
