import os
import smtplib

from flask import Flask, render_template, request

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

EMAIL = "cuongphong2508@gmail.com"
PASSWORD = os.getenv('PASSWORD')

posts = [{"id": 1,
          "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts "
                  "black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water "
                  "chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko "
                  "chicory celtuce parsley jícama salsify.",
          "title": "The Life of Cactus", "subtitle": "Who knew that cacti lived such interesting lives."},
         {"id": 2,
          "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red "
                  "dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad "
                  "power cord steal the warm chair right after you get up for purr for no reason leave hair "
                  "everywhere, decide to want nothing to do with my owner today.",
          "title": "Top 15 Things to do When You are Bored",
          "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities."},
         {"id": 3,
          "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes "
                  "bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish "
                  "chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie "
                  "roll marshmallow halvah carrot cake.",
          "title": "Introduction to Intermittent Fasting", "subtitle": "Learn about the newest health craze."}]

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.get("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.post("/contact")
def receive_data():
    data = request.form
    name = data['name']
    email = data['email']
    phone = data['phone']
    message = data['message']
    new_h1 = "Successfully sent your message"
    send_email(name, email, phone, message)
    return render_template("contact.html", new_h1=new_h1)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
