from flask import Flask, render_template

app = Flask(__name__)


@app.route('/api/ping')
def hello_world():
    return 'ok'

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
