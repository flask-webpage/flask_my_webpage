from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first_choice')
def first_choice():
    return render_template('first_choice.html')

if __name__ == '__main__':
    app.run(debug=True)