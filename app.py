from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    read = db.Column(db.Boolean, default=False)

@app.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username}), 201

@app.route('/messages', methods=['POST'])
def send_message():
    sender_id = request.json.get('sender_id')
    recipient_id = request.json.get('recipient_id')
    content = request.json.get('content')
    message = Message(sender_id=sender_id, recipient_id=recipient_id, content=content, timestamp=datetime.now())
    db.session.add(message)
    db.session.commit()
    return jsonify({'id': message.id, 'content': message.content}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    recipient_id = request.args.get('recipient_id')
    messages = Message.query.filter_by(recipient_id=recipient_id).all()
    return jsonify([{'id': m.id, 'sender_id': m.sender_id, 'content': m.content, 'timestamp': m.timestamp.isoformat(), 'read': m.read} for m in messages])

@app.route('/messages/<int:message_id>', methods=['PATCH'])
def mark_message_as_read(message_id):
    message = Message.query.get_or_404(message_id)
    message.read = True
    db.session.commit()
    return jsonify({'id': message.id, 'content': message.content, 'read': message.read}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)

