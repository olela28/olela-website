from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

@app.route("/projects", methods=["GET"])
def projects():
        return render_template("projects.html")