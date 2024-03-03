from flask import Blueprint, render_template
import requests

main = Blueprint('main', __name__)

# Move your posts fetching here or to a better-suited place like a model
posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

@main.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)