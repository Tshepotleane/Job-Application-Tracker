from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "applications.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            date_applied TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def index():
    connection = get_db_connection()

    applications = connection.execute(
        "SELECT * FROM applications ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        applications=applications
    )


@app.route("/add", methods=["POST"])
def add_application():
    company = request.form["company"]
    position = request.form["position"]
    date_applied = request.form["date_applied"]
    status = request.form["status"]

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO applications
        (company, position, date_applied, status)
        VALUES (?, ?, ?, ?)
        """,
        (company, position, date_applied, status)
    )

    connection.commit()
    connection.close()

    return redirect("/")


@app.route("/edit/<int:application_id>", methods=["GET", "POST"])
def edit_application(application_id):

    connection = get_db_connection()

    if request.method == "POST":

        company = request.form["company"]
        position = request.form["position"]
        date_applied = request.form["date_applied"]
        status = request.form["status"]

        connection.execute(
            """
            UPDATE applications
            SET company = ?,
                position = ?,
                date_applied = ?,
                status = ?
            WHERE id = ?
            """,
            (
                company,
                position,
                date_applied,
                status,
                application_id
            )
        )

        connection.commit()
        connection.close()

        return redirect("/")

    application = connection.execute(
        "SELECT * FROM applications WHERE id = ?",
        (application_id,)
    ).fetchone()

    connection.close()

    return render_template(
        "edit.html",
        application=application
    )


@app.route("/delete/<int:application_id>")
def delete_application(application_id):

    connection = get_db_connection()

    connection.execute(
        "DELETE FROM applications WHERE id = ?",
        (application_id,)
    )

    connection.commit()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    create_database()
    app.run(debug=True)