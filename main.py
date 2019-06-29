from flask import Flask, render_template, request
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

with open('config.json','r') as config:
    params=json.load(config)["parameters"]

app = Flask(__name__)
if params['local_server']:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else :
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
    s_no,name,ph_no,email,msg,date
    '''
    s_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    ph_no = db.Column(db.String(12), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=False, nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)

class Posts(db.Model):
    '''
    s_no,slug,title,content,date
    '''
    s_no = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(25), unique=False, nullable=False)
    title = db.Column(db.String(20), unique=False, nullable=False)
    content = db.Column(db.String(20), unique=False, nullable=False)
    date = db.Column(db.String(12), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()[0:5]
    return render_template('index.html', params=params, posts=posts)

@app.route("/post/<string:post_slug>", methods = ['GET'])
def post_page(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/about")
def about():
    return render_template('about.html', params=params)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add Entry to the ds'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('ph_no')
        message = request.form.get('msg')

        '''
            s_no,name,ph_no,email,msg,date
            '''
        entry = Contacts(name=name, ph_no=phone, email=email, msg=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html', params=params)

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        name = request.form.get('username')
        apass = request.form.get('password')

        if (name == params['admin_name'] and apass == params['admin_pass']):
            posts = Posts.query.filter_by().all()[Posts.s_no:0:-1]
            return render_template('dashboard.html', params=params,posts=posts)

    return render_template('login.html')




app.run(debug=True)
