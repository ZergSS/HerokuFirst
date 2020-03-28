from flask import Flask, render_template
import flask
import pickle
import sklearn

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return render_template('my_model.html')

    if flask.request.method == 'POST':
        with open('my_model.pkl', 'rb') as fh:
            loaded_model = pickle.load(fh)
        totsp = float(flask.request.form['totsp'])
        livesp = float(flask.request.form['livesp'])
        kitsp = float(flask.request.form['kitsp'])
        dist = float(flask.request.form['dist'])
        metrdist = float(flask.request.form['metrdist'])
        walk = int(flask.request.form['walk'])
        floor = int(flask.request.form['floor'])
        code = int(flask.request.form['code'])

        price = loaded_model.predict([[totsp, livesp, kitsp, dist, code, metrdist, walk, floor]])
        return render_template('my_model.html', result=price)

if __name__ == '__main__':
    app.run()
    
# heroku login
# git init
# git add .
# git commit -m 'name commit'
# git push heroku master