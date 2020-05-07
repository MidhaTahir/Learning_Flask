from flask import Flask,render_template,request,session,flash
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #will return a dictionary instead of tuple
mysql = MySQL(app)

app.config['SECRET_KEY'] = os.urandom(24) #anyone who has this key can view user's session , rightnow its random 24 string

@app.route('/',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        try:
            form = request.form
            name = form['name']
            age = form['age']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO client(name,age) VALUES(%s,%s)",(name,age))
            mysql.connection.commit()
            flash('Successfully inserted data','success')
        except:
            flash('Failed to insert data','danger') #second parameter is category
    return render_template('index.html')

@app.route('/clients')
def clients():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM client")
    if result_value > 0:
        clients = cur.fetchall()
        print(clients)
        session['username'] = clients[0]['name'] #who is visiting our site
        return render_template('clients.html',clients=clients)

if __name__ == '__main__':
    app.run(debug=True)