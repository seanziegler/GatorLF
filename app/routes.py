from app import app
from flask import render_template
from app.forms import LostForm

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/lost')
def lost():
    form = LostForm()
    return render_template('lost.html', form = form)
