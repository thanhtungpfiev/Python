import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    your_name = "Dao Thanh Tung"
    return render_template("index.html", random_number=random_number, current_year=current_year, your_name=your_name)


if __name__ == "__main__":
    app.run(debug=True)
