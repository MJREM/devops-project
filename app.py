from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():

    conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

    cur = conn.cursor()

    cur.execute("SELECT * FROM employees")

    employees = cur.fetchall()

    cur.close()
    conn.close()

    html = "<h1>Employees</h1>"

    for emp in employees:
        html += f"<p>{emp[0]} - {emp[1]} - {emp[2]}</p>"

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)