import requests
from flask import Flask, render_template

from post_manager import PostManager

app = Flask(__name__)

post_manager = PostManager()


@app.route('/')
def home():
    headers = {'Accept': 'application/json'}
    blog_url = "https://api.npoint.io/d6415f70defc1e14e9be"
    response = requests.get(blog_url, headers=headers)
    response.raise_for_status()
    post_manager.init_blog_posts(response.json())
    return render_template("index.html", blog_posts=response.json())


@app.route('/post/<blog_id>')
def get_post(blog_id):
    blog_post = post_manager.blog_posts[blog_id]
    return render_template("post.html", blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
