#pylint: disable-all
import json
from flask import Flask, render_template, request, session
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection details
db_connection = psycopg2.connect(
    host="localhost",
    port="5433",
    database="news_app",
    user="postgres",
    password="password"
)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user_id' not in session:
        return "You need to log in first."

    user_id = session['user_id']

    if request.method == 'POST':
        # Retrieve updated preferences from the form
        theme = request.form['theme']
        language = request.form['language']
        # Handle more preferences as needed

        # Update preferences in the "data" table
        with db_connection.cursor() as cursor:
            cursor.execute("""
                UPDATE data
                SET preferences = %s
                WHERE user_id = %s
            """, (json.dumps({'theme': theme, 'language': language}), user_id))

        db_connection.commit()

    # Retrieve user preferences from the "data" table
    with db_connection.cursor() as cursor:
        cursor.execute("""
            SELECT preferences FROM data WHERE user_id = %s
        """, (user_id,))
        row = cursor.fetchone()
        preferences = json.loads(row[0]) if row else {}

    return render_template('home.html', preferences=preferences)

if __name__ == '__main__':
    app.run()
