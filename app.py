from cat_api import CatApi
from flask import Flask, render_template

api = CatApi()


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/breeds')
def breeds():
    breeds = api.get_breeds()
    return render_template('breeds.html', breeds=breeds)

@app.route('/breed/<id>')
def breed(id):
    breed_img = api.get_breed_img(id)
    return render_template('breed.html', breed_img=breed_img)

if __name__ == '__main__':
    print('run')
    app.run(debug=True)

