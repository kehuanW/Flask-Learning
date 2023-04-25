from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
    return "<h1>Hello World</h1>"

@app.route('/p1') # 127.0.0.1:5000/p1
def info():
    return "<h1>page 1</h1>"

@app.route('/person/<name>')
def person(name):
    return "<h1>This is a person for {} </h1>".format(name.upper())

# TODO: I am not sure why it runs well...... shit
@app.route('/page/<num>')
def page(num):
    # num = [1,2,3]
    return "<h1>This is a page for {} </h1>".format(num[100])

if __name__ == '__main__':
    # No debug True in production environment
    app.run(debug=True)