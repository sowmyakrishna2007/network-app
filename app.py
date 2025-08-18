from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"
model = SentenceTransformer("all-mpnet-base-v2")

DB_FILE = "users.db"

def normalize(vecs):
    return vecs / np.linalg.norm(vecs, axis=1, keepdims=True)

# ---------- Database Setup ----------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS profiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    description TEXT NOT NULL,
                    goals TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

init_db()

# ---------- DB Helpers ----------
def add_account(username, email, hashed_pw):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO accounts (username, email, password) VALUES (?, ?, ?)",
              (username, email, hashed_pw))
    conn.commit()
    conn.close()

def add_profile(username, description, goals):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO profiles (username, description, goals) VALUES (?, ?, ?)",
              (username, description, ",".join(goals)))
    conn.commit()
    conn.close()

def get_account_by_username(username):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT username, email, password FROM accounts WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"username": row[0], "email": row[1], "password": row[2]}
    return None

def get_all_profiles():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT username, description, goals FROM profiles")
    rows = c.fetchall()
    conn.close()
    return [{"username": r[0], "description": r[1], "goals": r[2].split(",")} for r in rows]

# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))

    top_matches = []
    users = get_all_profiles()

    if request.method == "POST":
        current_user = session["username"].strip().lower()
        print("Session username (normalized):", current_user)
        print("Profiles from DB:", [u["username"] for u in users])

        if len(users) >= 2:
            # Prepare goals strings
            for user in users:
                user["goals_str"] = " ".join(user["goals"])

            descriptions = [u["description"] for u in users]
            goals_combined = [u["goals_str"] for u in users]

            # Compute normalized embeddings
            desc_embeddings = normalize(model.encode(descriptions, convert_to_numpy=True))
            goal_embeddings = normalize(model.encode(goals_combined, convert_to_numpy=True))
            print(current_user)

            # Find index of current user
            
            ind = None
            for i, u in enumerate(users):
                print(u)
                if u["username"].strip().lower() == current_user:
                    ind = i
                
            
            print("Current user index:", ind)

            if ind is not None:
                scores = []
                for i, user in enumerate(users):
                    if i == ind:
                        continue
                    score_desc_to_goals = cosine_similarity([desc_embeddings[ind]], [goal_embeddings[i]])[0][0]
                    score_goals_to_desc = cosine_similarity([desc_embeddings[i]], [goal_embeddings[ind]])[0][0]
                    avg_score = 0.3 * score_desc_to_goals + 0.7 * score_goals_to_desc
                    scores.append((user["username"], user["description"], user["goals"], avg_score))

                # Sort by highest average score
                scores.sort(key=lambda x: x[3], reverse=True)
                top_matches = scores[:2]
                print("Top matches:", top_matches)

    return render_template("home.html", username=session["username"], top_matches=top_matches)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"].strip().lower()
        email = request.form["email"].strip()
        password = request.form["password"]
        description = request.form["description"].strip()
        goals = request.form.getlist("goals")
        goals = [g.strip() for g in goals if g.strip()]

        if get_account_by_username(username):
            return render_template("signup.html", error="Username already exists.")

        hashed_pw = generate_password_hash(password)
        add_account(username, email, hashed_pw)
        add_profile(username, description, goals)

        session["username"] = username
        return redirect(url_for("home"))

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip().lower()
        password = request.form["password"]

        user = get_account_by_username(username)
        if user and check_password_hash(user["password"], password):
            session["username"] = username
            return redirect(url_for("home"))
        return render_template("login.html", error="Invalid credentials.")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
