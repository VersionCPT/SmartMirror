from flask import render_template, jsonify, json, request, send_file, abort
from app import app, n, w
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

@app.route('/get_file', methods=['GET','POST'])
def get_file():
    file_name = request.args.get('file')
    if file_name is not None:
        try:
            return send_file(os.path.dirname(os.path.realpath(__file__))+"/files/"+file_name, as_attachment=True)
        except Exception as e:
            abort(400)
    else:
        abort(400)

@app.route('/get_news', methods=['GET', 'POST'])
def get_news():
    category = request.args.get('category')
    if category is None:
        abort(400)
    else:
        try:
            if n.news[category] is None:
                abort(400)
            else:
                data = json.dumps(n.news[category], ensure_ascii=False)
                return data
        except Exception as e:
            abort(400)

@app.route('/get_weather', methods=['GET','POST'])
def get_weather():
    info = w.get_weather()
    return json.dumps(info, ensure_ascii=False)