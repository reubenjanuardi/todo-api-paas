from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

app = Flask(__name__)

database_url = os.getenv('DATABASE_URL')

if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {
        "sslmode": "require"
    }
}

db = SQLAlchemy(app)

# MODEL DATABASE
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at
        }

# HOME
@app.route('/')
def home():
    return jsonify({
        "message": "Todo API PaaS Running",
        "version": "1.0.0"
    })

# HEALTH CHECK
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

# GET ALL TASKS
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()

    return jsonify([
        task.to_dict() for task in tasks
    ])

# CREATE TASK
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    new_task = Task(
        title=data['title'],
        description=data.get('description', '')
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "message": "Task created successfully"
    }), 201

# UPDATE TASK
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)

    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully"
    })

# DELETE TASK
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)