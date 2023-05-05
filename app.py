from flask import Flask, render_template, request
from auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route("/")
def hello():
    return "helo"

@app.route("/", methods=["POST"])
def handlePost():
    return request.form["name"]

@app.route("/about")
def about():
    return "this is about page"

@app.route("/user/<name>")
def user(name):
    return render_template("profile.html",name=name)

if __name__== "__main__":
    app.run(debug=True)