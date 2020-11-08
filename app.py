from flask import Flask, render_template, request

import pickle
 
model = pickle.load(open('/home/amninder/Documents/project/wtwn-anime/mymodel.pkl',"rb"))

app = Flask(__name__)

@app.route("/")

def base():
    return render_template('home.html')
@app.route('/predict',method=['POST'])

def home():
    da = request.form['a']
    pre = model.predict(da)
    return render_template('after.html',data = pre)

if __name__ == "__main__":
    app.run(debug = True)