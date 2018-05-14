from flask import render_template, json, request, send_file, abort, Markup
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
                ret = ""
                for i in n.news[category]:
                    ret = ret + "<news>" + "<title>" + i[0] + "</title>" + "<content>" + i[1] + "</content>" + "</news>"
                #data = json.dumps(n.news[category], ensure_ascii=False)
                #return data
                return Markup(ret)
        except Exception as e:
            abort(400)

@app.route('/get_weather', methods=['GET','POST'])
def get_weather():
    info = w.get_weather()
    ret = ""
    for i in info.keys():
        ret = ret + "<" + str(i) + ">" + str(info[i]) + "</" + str(i) + ">"
    return Markup(ret)
    #return json.dumps(info, ensure_ascii=False)

@app.route('/face_upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save("face/"+file.filename)
        return file.filename+"uploaded"
    else:
        return '''<!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>'''