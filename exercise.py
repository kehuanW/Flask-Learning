from flask import Flask

app = Flask(__name__)

@app.route('/puppy-name/<in_name>')
def index(in_name):
    if in_name[-1] != "y":
        out_name = in_name + "y"
    else:
        out_name = in_name[:-1] + "iful"

    return "<h1>The puppy name is {}</h1>".format(out_name)

if __name__ == '__main__':
    app.run(debug=True)