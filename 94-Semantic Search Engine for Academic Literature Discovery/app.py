from flask import Flask, render_template, request, redirect, session
import json
from model import semantic_search

app = Flask(__name__)
app.secret_key = "semantic_secret"

USER_FILE = "users.json"

# Load users
def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

# Save users
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

@app.route("/")
def home():
    return redirect("/login")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = load_users()
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "User already exists!"

        users[username] = password
        save_users(users)
        return redirect("/login")

    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = load_users()
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid credentials!"

    return render_template("login.html")

# Dashboard
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        query = request.form["query"]
        results = semantic_search(query)
        return render_template("results.html", results=results.to_dict(orient="records"))

    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=False)