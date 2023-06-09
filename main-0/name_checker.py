from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("name_checker_base.html")

@app.route('/home')
def home():
    return render_template("name_checker_home.html")

@app.route('/result')
def result():
    username = request.args.get('username')

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    report = lower_letter and upper_letter and num_end

    return render_template('name_checker_result.html', 
    username=username, 
    report = report,
    lower=lower_letter, 
    upper=upper_letter, 
    num_end=num_end
    )

if __name__ == "__main__":
    app.run(debug=True)