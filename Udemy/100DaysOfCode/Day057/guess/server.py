import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/guess/<username>')
def guess(username):
    params = {'name': username}

    gender_url = "https://api.genderize.io"
    response = requests.get(gender_url, params=params)
    gender = response.json().get('gender')

    age_url = "https://api.agify.io"
    response = requests.get(age_url, params=params)
    age = response.json().get('age')

    return render_template("index.html", username=username.title(), gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
