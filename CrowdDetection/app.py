from flask import Flask,render_template,request,flash,redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':





 app.run(debug=True)
