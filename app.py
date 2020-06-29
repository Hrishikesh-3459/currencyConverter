from flask import Flask, render_template, request

app = Flask(__name__)


OTHER_TO_INR = {'USD': 75.57, 'EURO': 85.03, 'GBP': 93.33, 'AUD': 51.91}
INR_TO_OTHER = {'USD': 0.013, 'EURO': 0.012, 'GBP': 0.011, 'AUD': 0.019}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        currency = INR_TO_OTHER.values()
        return render_template("index.html", currency = currency)
    else:
        frm = request.form.get("from")
        to = request.form.get("to")
        return render_template('output,html', frm = frm, to = to)
