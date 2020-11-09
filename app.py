from flask import Flask, render_template, request

import pickle

# def main():
file = "prediction/myanimemodel.pkl"
fileobj = open(file,'rb')
mp = pickle.load(fileobj)
# print(mp('Naruto: Shippuuden'))
app = Flask(__name__, template_folder='./template', static_folder='./static')

@app.route("/")

def home():
    # return "hi"
    return (render_template('index.html'))

@app.route('/predict',method=['POST','GET'])

def model():
    da = request.form.values()
    pre = mp(da)
    return render_template('after.html',data = pre)


if __name__ == "__main__":
    app.run(debug=True)