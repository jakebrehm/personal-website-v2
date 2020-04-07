from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/epicycler/')
def epicycler():
    return render_template('epicycler.html')

if __name__ == '__main__':
    app.run(debug=True)