from flask import Flask, render_template, request
import requests
import smtplib
from INFO import MY_EMAIL, PASSWORD, RECEIVER_EMAIL


posts = requests.get("https://api.npoint.io/0fdc688b3ef82bbd2567").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")

def send_email(details):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject: New Visitor\n\n{details}"
        )

@app.route("/contact",methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        details = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """
        print(details)
        send_email(details)
        return render_template("contact.html", msg_sent=True)
        
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
