from flask import render_template, Blueprint, request

core = Blueprint('core', __name__)

@core.route('/')
@core.route('/home')
def index():
    return render_template('index.html')