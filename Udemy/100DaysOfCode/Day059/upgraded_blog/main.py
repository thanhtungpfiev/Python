from flask import Flask, render_template

app = Flask(__name__)

# headers = {'Accept': 'application/json'}
# post_url = "https://api.npoint.io/c790b4d5cab58020d391"
# proxies = {
#     "http": "http://rb-proxy-apac.bosch.com:8080"
# }
# response = requests.get(post_url, headers=headers, proxies=proxies)
# response.raise_for_status()

all_posts = [
    {
        "id": 1,
        "title": "The Life of Cactus",
        "subtitle": "Who knew that cacti lived such interesting lives.",
        "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.",
        "author": "Dao Thanh Tung",
        "date": "July 24, 2023"
    },
    {
        "id": 2,
        "title": "Top 15 Things to do When You are Bored",
        "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
        "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.",
        "author": "Dao Thanh Tung",
        "date": "July 25, 2023"
    },
    {
        "id": 3,
        "title": "Introduction to Intermittent Fasting",
        "subtitle": "Learn about the newest health craze.",
        "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.",
        "author": "Dao Thanh Tung",
        "date": "July 26, 2023"
    }
]


@app.route("/")
def get_all_posts():
    return render_template('index.html', all_posts=all_posts)


@app.route("/about")
def get_about():
    return render_template('about.html')


@app.route("/contact")
def get_contact():
    return render_template('contact.html')


@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = {}
    for post_temp in all_posts:
        if post_temp['id'] == post_id:
            post = post_temp
            break
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
