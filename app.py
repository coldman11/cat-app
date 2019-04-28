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





api.get_image()






#if __name__ == '__main__':
    #print('run')
    #app.run(debug=True)

