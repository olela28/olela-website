from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route("/projects")
def projects():
    return render_template("/projects.html")