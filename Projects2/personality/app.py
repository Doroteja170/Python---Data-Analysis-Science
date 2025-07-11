from flask import Flask, render_template, request, redirect, url_for
import joblib
import json
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")
with open("class_dict.json", "r") as f:
    class_dict = json.load(f)


index_to_label = {v: k for k, v in class_dict.items()}

@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        try:
            
            answers = [int(request.form[f"q{i}"]) for i in range(1, 10)]
            features = np.array(answers).reshape(1, -1)

            prediction = model.predict(features)[0]
            personality = index_to_label[prediction]

            if personality == "Introvert":
                return render_template("introvert.html")
            elif personality == "Extrovert":
                return render_template("extrovert.html")
            elif personality == "Ambivert":
                return render_template("ambivert.html")
            else:
                return "Unknown personality type predicted", 500
        except Exception as e:
            return f"Error: {str(e)}", 400

    return render_template("survey.html")

if __name__ == "__main__":
    app.run(debug=True)
