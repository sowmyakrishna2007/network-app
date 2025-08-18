import sqlite3
from werkzeug.security import generate_password_hash

# Connect to (or create) the database
conn = sqlite3.connect("users.db")
c = conn.cursor()

# Drop old tables if they exist
c.execute("DROP TABLE IF EXISTS accounts")
c.execute("DROP TABLE IF EXISTS profiles")

# Create fresh tables
c.execute("""
CREATE TABLE accounts (
    username TEXT PRIMARY KEY,
    email TEXT,
    password TEXT
)
""")

c.execute("""
CREATE TABLE profiles (
    username TEXT PRIMARY KEY,
    description TEXT,
    goals TEXT
)
""")

# Sample users (name, description, [goals])
sample_users = [
    ("Alice", "Loves hiking and photography.", ["Climb Kilimanjaro", "Start a travel blog"]),
    ("Bob", "Software developer into AI and robotics.", ["Build a home robot", "Contribute to open-source AI projects"]),
    ("Charlie", "Teacher passionate about education reform.", ["Write a book on teaching", "Create free online lessons"]),
    ("Diana", "Fitness coach and nutrition enthusiast.", ["Run a marathon", "Launch a fitness podcast"]),
    ("Ethan", "Musician exploring world music.", ["Record an album", "Collaborate with international artists"]),
    ("Fiona", "Gardener and sustainability advocate.", ["Start a community garden", "Teach composting workshops"]),
    ("George", "Entrepreneur in green tech.", ["Develop a solar startup", "Speak at climate conferences"]),
    ("Hannah", "Chef experimenting with fusion cuisine.", ["Open a restaurant", "Publish a cookbook"]),
    ("Ian", "Student interested in neuroscience.", ["Research brain-computer interfaces", "Get published in a science journal"]),
    ("Jade", "Photographer focusing on wildlife.", ["Photograph endangered species", "Host an exhibition"]),
    ("Kyle", "Gamer and game developer.", ["Release an indie game", "Stream game dev on Twitch"]),
    ("Lara", "Writer and poet.", ["Publish a poetry collection", "Host spoken word events"]),
    ("Mason", "Engineer fascinated by space travel.", ["Work at SpaceX", "Design a satellite"]),
    ("Nina", "Dancer and choreographer.", ["Perform internationally", "Teach dance in schools"]),
    ("Oscar", "Doctor volunteering in rural areas.", ["Open a free clinic", "Train local healthcare workers"]),
    ("Paula", "Marine biologist.", ["Research coral reefs", "Educate communities on ocean conservation"]),
    ("Quinn", "Fashion designer.", ["Launch a sustainable clothing line", "Show at Fashion Week"]),
    ("Ravi", "Data scientist.", ["Win a Kaggle competition", "Build a nonprofit analytics team"]),
    ("Sophie", "Yoga instructor.", ["Host retreats abroad", "Write a book on mindfulness"]),
    ("Tom", "Historian researching ancient cultures.", ["Publish historical research", "Create a documentary"])
]

# Insert sample data
for name, desc, goals in sample_users:
    email = f"{name.lower()}@example.com"
    password_hash = generate_password_hash("password123")  # Default password
    goals_str = ", ".join(goals)

    c.execute("INSERT INTO accounts (username, email, password) VALUES (?, ?, ?)",
              (name, email, password_hash))
    c.execute("INSERT INTO profiles (username, description, goals) VALUES (?, ?, ?)",
              (name, desc, goals_str))

# Commit and close
conn.commit()
conn.close()

print("Database initialized with fresh sample data.")
