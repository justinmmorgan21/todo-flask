from flask import Flask, request
import db

app = Flask(__name__)

@app.route("/tasks.json")
def index():
    return db.tasks_all()

@app.route("/tasks.json", methods=["POST"])
def create():
    name = request.form.get("name")
    estimated_time = request.form.get("estimated_time")
    deadline = request.form.get("deadline")
    return db.tasks_create(name, estimated_time, deadline)

@app.route('/')
def hello():
    return 'Hello, World!'