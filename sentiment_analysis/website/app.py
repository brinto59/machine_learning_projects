from flask import Flask, render_template, flash
from model_file import transform_text
from form_fields import PredictForm
import pickle


app = Flask(__name__)
app.config["SECRET_KEY"] = "you_will_never_guess"

with open("../model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/', methods=["GET", "POST"])
def home():
    form = PredictForm()
    if form.validate_on_submit():
        print(form.review.data)
        prediction = model.predict([form.review.data])
        flash(prediction)
    return render_template("index.html", title="Sentiment Analysis", form=form)


if __name__ == "__main__":
    app.run(debug=True)


