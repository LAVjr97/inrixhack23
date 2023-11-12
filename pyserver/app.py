from flask import Flask, render_template, request
import transport

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("results.tsx") # with data from API
    else:
        return render_template("index.tsx")

@app.route("/results", methods=["GET"])
def results():
    return {"results": ["Results page", "results", "done"]}

if __name__ == "__main__":
    app.run(debug=True)