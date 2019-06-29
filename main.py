from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index")
def rehome():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/recipes")
def recipes():
    return render_template('recipes.html')

app.run(debug=True)
