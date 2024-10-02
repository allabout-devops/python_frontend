from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-welcome')
def get_welcome():
    response = requests.get('http://127.0.0.1:5001/api/welcome')
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  # Run on port 5000
