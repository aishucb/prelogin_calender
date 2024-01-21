from flask import Flask,render_template
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
    try:
        mysql_connection = mysql.connector.connect(**mysql_db_config)
        if mysql_connection.is_connected():
            cursor = mysql_connection.cursor()
            query = "SELECT name, description, timestart FROM mdl_event ORDER BY timestart DESC LIMIT 4;"
            cursor.execute(query)
            last_four_records = cursor.fetchall()

            # Extracting names, descriptions, and timestarts from the fetched records
            names = [record[0] for record in last_four_records]
            descriptions = [record[1] for record in last_four_records]
            timestarts = [record[2] for record in last_four_records]

            return render_template('event.html', names=names, descriptions=descriptions, timestarts=timestarts)

    except Exception as e:
        # Handle exceptions appropriately (e.g., log the error)
        print(f"Error: {e}")

    finally:
        # Close the database connection in the 'finally' block to ensure it's always closed
        if mysql_connection.is_connected():
            cursor.close()
            mysql_connection.close()

if __name__ == '__main__':
    app.run(debug=True)
