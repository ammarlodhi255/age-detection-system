import os
from Model import Model
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request

app = Flask(__name__)
model = Model()


@app.route("/")
def Start():
    return render_template('index.html')


@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        file = request.files['image']
        fileName = os.path.join(
            'D:\\Project\Project\\static\\', secure_filename(file.filename))
        file.save(fileName)
        age = model.predict(fileName)
        return render_template("predict.html", predicted_age=age, src=fileName)
    return render_template('index.html')


app.run(debug=True)
