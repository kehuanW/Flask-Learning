from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("name_checker_home.html")

if __name__ == "__main__":
    app.run(debug=True)