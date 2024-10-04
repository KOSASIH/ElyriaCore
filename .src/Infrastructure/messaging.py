from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://user:password@host:port/dbname'
mongo = PyMongo(app)

@app.route('/messages', methods=['POST'])
def create_message():
    message_data = request.get_json()
    message = mongo.db.messages.insert_one(message_data)
    return jsonify({'message_id': message.inserted_id}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = mongo.db.messages.find()
    return jsonify([message for message in messages])

@app.route('/messages/<message_id>', methods=['GET'])
def get_message(message_id):
    message = mongo.db.messages.find_one({'_id': message_id})
    if message:
        return jsonify(message)
    else:
        return jsonify({'error': 'Message not found'}), 404

@app.route('/messages/<message_id>', methods=['PUT'])
def update_message(message_id):
    message_data = request.get_json()
    message = mongo.db.messages.update_one({'_id': message_id}, {'$set': message_data})
    if message:
        return jsonify({'message': 'Message updated'})
    else:
        return jsonify({'error': 'Message not found'}), 404

@app.route('/messages/<message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = mongo.db.messages.delete_one({'_id': message_id})
    if message:
        return jsonify({'message': 'Message deleted'})
    else:
        return jsonify({'error': 'Message not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
