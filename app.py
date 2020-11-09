from flask import Flask, render_template, request, abort

# import anime_model
from anime_model import predict

app = Flask(__name__, template_folder='./template', static_folder='./static')

@app.route("/")

def home():
    # return "hi"
    return (render_template('index.html'))

@app.route('/predict', methods=("POST", "GET"))

def predict_on():
    # return  mp('Naruto: Shippuuden')
    anime = (request.form['anime'])
    # da = 'Naruto'
    # return da
    
    fg = predict((anime))

    
    return render_template('after.html',  tables=[fg.to_html(classes='data', header="true")])

@app.errorhandler(500)
def internal_error(e):
    print(e)
    return render_template("template/500.html")


if __name__ == "__main__":
    app.run()