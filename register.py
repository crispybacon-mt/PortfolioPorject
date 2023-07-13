#pylint: disable-all
import json
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Database connection details
db_connection = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_username",
    password="your_password"
)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']

        # Save user details to the "user" table
        with db_connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO "user" (user_name, email, password, name)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (username, email, password, name))
            user_id = cursor.fetchone()[0]

            # Initialize user preferences to an empty dictionary
            preferences = {}

            # Save user preferences to the "data" table
            cursor.execute("""
                INSERT INTO data (user_id, email, password, preferences)
                VALUES (%s, %s, %s, %s)
            """, (user_id, email, password, json.dumps(preferences)))

        db_connection.commit()
        return "Registration successful!"

    return render_template('/home.html')

if __name__ == '__main__':
    app.run()
