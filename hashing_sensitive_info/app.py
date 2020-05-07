from flask import Flask,render_template,request,session
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml
import os
from werkzeug.security import generate_password_hash,check_password_hash

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

# app.config['SECRET_KEY'] = os.urandom(24) #anyone who has this key can view user's session , rightnow its random 24 string

@app.route('/',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        form = request.form
        password = form['password']
        age = form['age']
        cur = mysql.connection.cursor()
        password = generate_password_hash(password) #encrypts password 
        cur.execute("INSERT INTO client(name,age) VALUES(%s,%s)",(password,age))
        mysql.connection.commit()
    return render_template('index.html')

@app.route('/clients')
def clients():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM client")
    if result_value > 0:
        clients = cur.fetchall()
        print(clients)
        return str(check_password_hash(clients[5]['name'],'sunday'))# it decrypts .. #5 is location of record in db like 
        ''' +------------------------------------------------------------------------------------------------+------+
            | name                                                                                           | age  |
            +------------------------------------------------------------------------------------------------+------+
            | Midha                                                                                          |    9 |
            | Midha                                                                                          |    4 |
            | missmidha                                                                                      |   21 |
            | midha                                                                                          |   21 |
            | midha                                                                                          |   21 |
            | pbkdf2:sha256:150000$gXLyOp6Z$b07861371ec8dd6f5ab5fc7fa35e953f20efb01605a66f8ab2a6f2738e60c8a8 |   21 |--> 5th index
            +------------------------------------------------------------------------------------------------+------+'''
        # return render_template('clients.html',clients=clients)

if __name__ == '__main__':
    app.run(debug=True)