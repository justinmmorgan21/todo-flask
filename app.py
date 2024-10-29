from flask import Flask, request
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app)

@app.route("/tasks.json")
def index():
    return db.tasks_all()

@app.route("/tasks.json", methods=["POST"])
def create():
    name = request.form.get("name")
    estimated_time = request.form.get("estimated_time")
    deadline = request.form.get("deadline")
    return db.tasks_create(name, estimated_time, deadline)

@app.route("/tasks/<id>.json")
def show(id):
    return db.tasks_find_by_id(id)

@app.route("/tasks/<id>.json", methods=["PATCH"])
def update(id):
    name = request.form.get("name")
    estimated_time = request.form.get("estimated_time")
    deadline = request.form.get("deadline")
    return db.tasks_update_by_id(id, name, estimated_time, deadline)

@app.route("/tasks/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.tasks_destroy_by_id(id)

@app.route('/')
def hello():
    return 'Hello, World!'