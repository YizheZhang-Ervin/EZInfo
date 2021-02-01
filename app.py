from flask import Flask, request
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS
from flask import jsonify, render_template, request
from translate import Translator
from imp import reload

# Initialize Flask
app = Flask(__name__,static_folder='static',template_folder='static')
api = Api(app)

# Cross Domain
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)
parser.add_argument('input', type=str)

# Basic Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        key = request.args.get('key', '')
        return render_template('index.html', data=key)

@app.route('/<string:gamename>', methods=['GET', 'POST'])
def gameChoice(gamename):
    page = "game.html"
    json = f"static/{gamename}/Build/Build.json"
    if request.method == 'GET':
        return render_template(page,gamename=gamename,json=json)
    elif request.method == 'POST':
        key = request.args.get('key', '')
        return render_template(page, data=key)

# RESTful API Route
class jsonAPI(Resource):
    def get(self,key):
        try:
            jsonObj = {"key":key}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})
    
    def post(self,key):
        try:
            args = parser.parse_args()
            key = eval(args['key'])
            jsonObj = {"key":key}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})
api.add_resource(jsonAPI, '/api/<key>')

class translatorAPI(Resource):
    def get(self):
        try:
            sentence = request.args.get("sentence","")
            fromlang = request.args.get("fromlang","")
            tolang = request.args.get("tolang","")
            translator_ec = Translator(from_lang=fromlang, to_lang=tolang)
            translatedSentence = translator_ec.translate(sentence)
            return jsonify({"result":translatedSentence})
        except Exception:
            return jsonify({"error":"error"})
api.add_resource(translatorAPI, '/api/translate/')

class fintechAPI(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            inputs = args['input']
            # 写入文件
            f = open('./online_codes/codes.py', 'w+')
            f.write(eval(inputs))
            f.close()
            # 重新导入文件中函数
            import online_codes.codes as oc
            reload(oc)
            # 返回运行结果
            temp = oc.Run.run()
            if type(temp) == dict:
                rst = {"x":temp.get("x",[]),"y":temp.get("y",[]),"y2":temp.get("y2",[]),"other":temp}
            else:
                rst = {"other":temp}
            return jsonify({"result":rst})
        except Exception:
            return jsonify({"error":"error"})
api.add_resource(fintechAPI, '/api/fintech/')

if __name__ == '__main__':
    app.run(debug=False)