from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)
@app.route('/')
def getmyweb():
    return render_template('index.html')
@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')
@app.route('/story.html')
def story():
    return render_template('story.html')
@app.route('/conclusion.html')
def conclusion():
    return render_template('conclusion.html')
    return render_template('image_render.html')