from flask import Flask, jsonify
from flask_cors import CORS 


app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources = {r"/*": {'origins':"*"}})
# or
# only reason why I chose localhost: 8080 cos vue is on that site
# but either way is fine
# CORS(app, resources = {r"/*": {'origins': 'http://127.0.0.1:8080/', 'allow_headers': 'Access-Control-Allow-Origin'}})

# for the moment going to keep it this way but will add MVC to make it 
# more neat... now to the frontend. 

@app.route('/ping')
def index():
    return "Welcome to Vue!"


if __name__ == "__main__":
    app.run(debug = True, port = 5001)