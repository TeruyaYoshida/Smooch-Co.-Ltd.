from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service1')
def service1():
    return render_template('service1.html')

@app.route('/members')
def members():
    return render_template('members.html')


if __name__ == '__main__':
    app.run()

