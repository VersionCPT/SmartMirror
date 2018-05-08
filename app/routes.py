from flask import render_template, jsonify, json, request, send_file
from app import app
import os

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/get_json', methods=['GET'])
def get_json():

    data = [{"name": "Ford", "models": ["Fiesta", "Focus", "Mustang"]}, {"name": "BMW", "models": ["320", "X3", "X5"]},
     {"name": "Fiat", "models": ["500", "Panda"]}]

    '''
    return jsonify(data)
    '''

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/get_file', methods=['GET'])
def get_file():
    file_name = request.args.get('file')
    if file_name is not None:
        return send_file(os.path.dirname(os.path.realpath(__file__))+"/files/"+file_name, as_attachment=True)