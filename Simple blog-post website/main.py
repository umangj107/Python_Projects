from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/6aca8e2d7173b77a43f8")
posts = response.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
