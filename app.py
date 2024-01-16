from flask import Flask
import mysql.connector
app = Flask(__name__)

@app.route('/')
def hello_world():
    mysql_db_config = {
    'host': '127.0.0.1',
    'user': 'vongle',
    'password': 'ashiv3377',
    'database': 'osqacademy',
}
    mysql_connection = mysql.connector.connect(**mysql_db_config)
    if mysql_connection.is_connected():
        cursor = mysql_connection.cursor()
        query = "select name,description,timestart from mdl_event;"
        cursor.execute(query)
        usernames = cursor.fetchall()
        for username_tuple in usernames:
            name,description,timestart = username_tuple
    return name+description+timestart

if __name__ == '__main__':
    app.run(debug=True)
