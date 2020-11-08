from flask import Flask, render_template, request

import pickle

file = "myanimemodel.pkl"
fileobj = open(file,'rb')
mp = pickle.load(fileobj)
# print(mp('Naruto: Shippuuden'))
app = Flask(__name__)

@app.route("/")

def base():
    return render_template('home.html')
@app.route('/predict',method=['POST'])

def home():
    da = request.form['a']
    pre = mp.model(da)
    return render_template('after.html',data = pre)

if __name__ == "__main__":
    app.run(debug = True)