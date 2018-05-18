
from flask import render_template, request, send_file, abort, Markup, jsonify
from app import app, n, w, User
import os

PROFILE_FOLDER = os.path.join('static', 'Image')
app.config['UPLOAD_FOLDER'] = PROFILE_FOLDER

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

    return jsonify(data)

@app.route('/recieve_file', methods=['GET','POST'])
def get_file():
    file_name = request.args.get('fileName')
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


@app.route('/recieve_image', methods = ['GET', 'POST'])
def send_image():
    file_name = request.args.get('fileName')
    if file_name is not None:
        try:
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            return render_template("image.html", user_image=full_filename)
        except Exception as e:
            abort(411)
    else:
        abort(411)


@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    user = User.User(data['id'], data['pw'], data['money'])
    return jsonify(user.getStr())
