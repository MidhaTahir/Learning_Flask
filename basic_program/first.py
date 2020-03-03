from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello There </h1>'

@app.route('/home',methods=['GET','POST']) #add /home to the address in chrome to see home page
def home():
    myvar = 'code'
    #to render the frontend template we put it in template folder and give it's file name in render_template
    return render_template('code.html',myvar=myvar) 

    
if __name__ == '__main__':
    #open cmd write ipconfig copy IPv4 Address and paste it in host below to make it visible in mobile too (remember to off your firewall private and public networks)
    app.run(debug=True,host='192.168.1.105')

