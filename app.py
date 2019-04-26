from cat_api import CatApi
from flask import Flask, render_template

api = CatApi()
breeds = api.get_breeds()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)