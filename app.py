from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS
from flask import jsonify, render_template, request

# Initialize Flask
app = Flask(__name__,static_folder='static',template_folder='static')
api = Api(app)

# Cross Domain
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

# Basic Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        key = request.args.get('key', '')
        return render_template('index.html', data=key)

@app.route('/game1', methods=['GET', 'POST'])
def game1():
    if request.method == 'GET':
        return render_template('game1.html')
    elif request.method == 'POST':
        key = request.args.get('key', '')
        return render_template('game1.html', data=key)

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

if __name__ == '__main__':
    app.run(debug=False)