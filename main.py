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
        similar_message = []
        if len(query) > 0:
            # check the data
            check_data = filter.predict(query)
            # set the data
            tipe = check_data['prediction']
            similar_message =check_data['similarity']
        return render_template("index.html", query=query, type=tipe, similarity=similar_message)
    else:
        return render_template("index.html")

# get acurracy score from the user

@app.route("/score", methods=['POST'])
def insert_data():
    filter.fit(request.form.get("message"), request.form.get("type"))
    return "it's work"

if __name__ == "__main__":
    app.run(debug=True)