from flask import Flask
from flask import request, render_template

# machine learning algorithm
from src import filter

app = Flask(__name__)

@app.route("/")
def home():
    if request.method == "GET":
        query = request.args.get('pesan', '')
        tipe = ''
        if len(query) > 0:
            tipe = filter.predict(query)
        return render_template("index.html", query=query, type=tipe)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)