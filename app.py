from flask import Flask,render_template,request,session,redirect,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost')
