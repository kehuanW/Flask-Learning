from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Jose"
    letters = list(name)
    pup_dic = {'pup_name': 'Sammy'}
    mylist = [1,2,3,4,5,6,7,8]
    return render_template('HTML.html', name=name, letters=letters, pup_dic=pup_dic, mylist=mylist )

if __name__ == '__main__':
    app.run(debug=True)