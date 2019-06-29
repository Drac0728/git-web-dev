from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi! I just created a page with flask"

@app.route("/about")
def about():
    name = "Sahaj"
    return render_template('about.html',name = name)
@app.route("/index")
def index():
    return render_template('index.html')

app.run(debug=True)
