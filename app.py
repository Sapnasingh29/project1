from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# -----------------------
# Login Page
# -----------------------
@app.route("/")
def home():
    return render_template("login.html")


# -----------------------
# Login Validation
# -----------------------
@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    # Temporary credentials
    if username == "admin" and password == "admin123":
        return redirect("/dashboard")

    return "<h2>Invalid Username or Password</h2>"


# -----------------------
# Dashboard
# -----------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -----------------------
# Employee List
# -----------------------
@app.route("/employees")
def employees():
    return render_template("employees.html")


# -----------------------
# Add Employee
# -----------------------
@app.route("/add-employee")
def add_employee():
    return render_template("add_employee.html")


# -----------------------
# Request Access
# -----------------------
@app.route("/request-access")
def request_access():
    return render_template("request_access.html")


# -----------------------
# Access Requests
# -----------------------
@app.route("/access-requests")
def access_requests():
    return render_template("access_requests.html")


# -----------------------
# Run Application
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
    
    