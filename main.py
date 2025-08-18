from flask import Flask, request, redirect, url_for, render_template_string
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')  # or another model
def normalize(vecs):
    return vecs / np.linalg.norm(vecs, axis=1, keepdims=True)


# 20 sample users with diverse goals and backgrounds
users = [
    
]




# HTML templates
form_template = """
<!DOCTYPE html>
<html>
<head><title>Create Profile</title></head>
<body>
  <h2>Create Your Profile</h2>
  <form method="post">
    Name: <input type="text" name="name" required><br>
    Description:<br>
    <textarea name="description" rows="3" cols="40" required></textarea><br>
    Goals (comma-separated):<br>
    <textarea name="goals" rows="2" cols="40" required></textarea><br><br>
    <input type="submit" value="Submit">
  </form>

  {% if users %}
    <hr>
    <h3>Current Users</h3>
    <ul>
      {% for user in users %}
        <li>{{ user['name'] }}</li>
      {% endfor %}
    </ul>
    <a href="{{ url_for('match') }}">See Matches</a>
  {% endif %}
</body>
</html>
"""

matches_template = """
<!DOCTYPE html>
<html>
<head><title>Matches</title></head>
<body>
  <h2>User Matches</h2>
  {% for name, matches in top_matches.items() %}
    <strong>{{ name }}</strong>:<br>
    {% for match_name, score in matches %}
      → {{ match_name }} (score: {{ score }})<br>
    {% endfor %}
    <br>
  {% endfor %}
  <a href="{{ url_for('home') }}">← Back</a>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        goals = [g.strip() for g in request.form["goals"].split(",") if g.strip()]
        users.append({"name": name, "description": description, "goals": goals})
        return redirect(url_for("home"))

    return render_template_string(form_template, users=users)

@app.route("/match")
def match():
    if len(users) < 2:
        return "<p>Need at least 2 users to show matches. <a href='/'>Back</a></p>"

    for user in users:
        user["goals_str"] = " ".join(user["goals"])

    descriptions = [u["description"] for u in users]
    goals_combined = [u["goals_str"] for u in users]

    desc_embeddings = normalize(model.encode(descriptions, convert_to_numpy=True))
    goal_embeddings = normalize(model.encode(goals_combined, convert_to_numpy=True))

    top_matches = {}
    for i, user in enumerate(users):
        scores = []
        for j, candidate in enumerate(users):
            if i == j:
                continue
            score_desc_to_goals = cosine_similarity([desc_embeddings[i]], [goal_embeddings[j]])[0][0]
            score_goals_to_desc = cosine_similarity([desc_embeddings[j]], [goal_embeddings[i]])[0][0]
            avg_score = (score_desc_to_goals + score_goals_to_desc) / 2
            scores.append((users[j]["name"], round(avg_score, 4)))
        scores.sort(key=lambda x: x[1], reverse=True)
        top_matches[user["name"]] = scores[:2]

    return render_template_string(matches_template, top_matches=top_matches)

if __name__ == "__main__":
    app.run(debug=True)

