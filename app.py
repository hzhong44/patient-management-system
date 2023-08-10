from functools import wraps

from flask import Flask, redirect, url_for, render_template, session, flash, request

from models.filter import Filter
from models.patient import PatientDAO
from models.user import UserDAO

app = Flask(__name__)
app.secret_key = "secret key"


def logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


@app.route('/')
def landing():  # put application's code here
    # redirects to dashboard if logged in, shows login otherwise
    return redirect(url_for("login"))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = UserDAO()
        if users.login(username, password):
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid email or password"
            return render_template("login.html", error=error)
    if session.get("logged_in", None) is True:
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route('/logout', methods=["GET", "POST"])
@logged_in
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/dashboard', methods=["GET", "POST"])
@logged_in
def dashboard(patients=None):
    # todo: pagination both for display and for fetching from db
    if patients is None:
        patientDAO = PatientDAO()
        patients = patientDAO.get_patients_list()

    return render_template("dashboard.html", patients=patients)


@app.route('/add_patient', methods=["GET", "POST"])
@logged_in
def patient_form():
    # client-side validation for name and date of birth
    if request.method == "POST":
        patient = PatientDAO()
        first_name = request.form.get("first_name")
        middle_name = request.form.get("middle_name")
        last_name = request.form.get("last_name")
        dob = request.form.get("dob")
        status = request.form.get("status")
        address = request.form.get("address")
        other = request.form.get("other")
        patient.add_patients([[first_name, middle_name, last_name, dob, status, address, other]])
        flash("Patient added successfully")
        return redirect(url_for("dashboard"))

    return render_template("patient_form.html")


@app.route('/search', methods=["GET", "POST"])
@logged_in
def search():
    if request.method == "POST":
        patient = PatientDAO()
        filter = Filter(patient.table_name)

        first_name = request.form.get("first_name")
        middle_name = request.form.get("middle_name")
        last_name = request.form.get("last_name")
        dob = request.form.get("dob")
        status = request.form.get("status")
        address = request.form.get("address")
        other = request.form.get("other")

        if first_name != "":
            filter.add_criteria("first_name", first_name)
        if middle_name != "":
            filter.add_criteria("middle_name", middle_name)
        if last_name != "":
            filter.add_criteria("last_name", last_name)
        if dob != "":
            filter.add_criteria("dob", dob)
        if status != "" and status is not None:
            filter.add_criteria("status", status)
        if address != "":
            filter.add_criteria("address", address)

        if len(filter.criteria) == 0:
            error = "Please enter at least one search parameter"
            return render_template("search.html", error=error)

        return dashboard(patient.select_query(filter.construct()))
    return render_template("search.html")


if __name__ == '__main__':
    app.run()
