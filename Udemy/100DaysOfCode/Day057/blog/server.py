import datetime
import random

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    your_name = "Dao Thanh Tung"
    return render_template("index.html", random_number=random_number, current_year=current_year, your_name=your_name)


@app.route('/blog/<num>')
def blog(num):
    headers = {'Accept': 'application/json'}
    blog_url = "https://api.npoint.io/d6415f70defc1e14e9be"
    response = requests.get(blog_url, headers=headers)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", all_posts=all_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)
