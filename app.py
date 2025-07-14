from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    username = request.form['username']
    return render_template('results1.html', name=username)

if __name__ == '__main__':
    app.run(debug=True)
