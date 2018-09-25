from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/artshow')
def artshow():
    return render_template('artshow.html', title='artshow')

if __name__ == '__main__':
    app.run()
