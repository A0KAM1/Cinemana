import flask
from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS
from bson.json_util import dumps, loads
from bson import ObjectId

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["DEBUG"] = True
cors = CORS(app)

myclient = MongoClient("mongodb://localhost:27017")
db = myclient.cinemana
collection = db['movies']

@app.route('/')
def Index():
    return "Hello World"

@app.route('/movies', methods=['GET'])
def GetBooks():
    movies = collection.find()
    res = [item for item in movies]
    return dumps(res)

@app.route('/movies/<string:id>', methods=['GET'])
def GetBookById(id):
    obj_id = ObjectId(id)
    res = collection.find_one({"_id": obj_id})
    return dumps(res)

@app.route('/movies/<string:id>', methods=['PUT'])
def UpdateBookById(id):
    book_req = request.get_json()
    obj_id = ObjectId(id)
    new_book = collection.find_one_and_update(
        {'_id': obj_id},
        {'$set': {
            'title': book_req['title'],
            'year': book_req['year']
        }},
        return_document=True
    )
    if new_book:
        return dumps(new_book)
    return jsonify({"massage": "Not Found"}), 404

@app.route('/movies', methods=['POST'])
def CreateNewBook():
    book_req = request.get_json()
    collection.insert_one(book_req)

    return jsonify(massage="Success")

@app.route('/movies/<string:id>', methods=['DELETE'])
def DeleteBookById(id): 
    obj_id = ObjectId(id)
    collection.delete_one({'_id': obj_id})
    return flask.jsonify(massage="Success")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)