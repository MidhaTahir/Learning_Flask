from flask import Flask,render_template,url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    fruits = ['apple','mango','banana']
    return render_template('index.html',fruits=fruits)

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True)