from flask import Flask, request
import flask
#from forms import PostForms
import transport
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

@app.route("/", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        dest = request.form.getlist('')
    optRoute = transport.calcBestRoute(dest[0], dest[1], dest[2], dest[3])
    return flask.jsonify(optRoute) 

if __name__ == "__main__":
    app.run(debug=True) 