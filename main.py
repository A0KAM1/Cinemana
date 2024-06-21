from flask import Flask, make_response, jsonify, request
from bd import Movies

app = Flask('Cinemana')
app.config['JSON_SORT_KEYS'] = False

@app.route('/movies', methods=['GET'])
def get_movies():
    return make_response(
        jsonify(Movies)
    )

@app.route('/movies', methods=['POST'])
def add_movie():
    res = request.json
    Movies.append(res)
    return res

app.run()