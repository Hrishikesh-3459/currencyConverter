from flask import Flask, render_template, request

app = Flask(__name__)


OTHER_TO_INR = {'USD': 75.57, 'EURO': 85.03, 'GBP': 93.33, 'AUD': 51.91, 'INR': 0.00}
INR_TO_OTHER = {'USD': 0.013, 'EURO': 0.012, 'GBP': 0.011, 'AUD': 0.019, 'INR': 0.00}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        currency = INR_TO_OTHER.keys()
        return render_template("index.html", currency = currency)
    else:
        frm = request.form.get("from")
        to = request.form.get("to")
        amt = request.form.get("amount")
        ans = calculate(frm, to, amt)
        return render_template('output.html', ans = ans)

def calculate(frm, to, amt):
    in_inr = OTHER_TO_INR[frm] * amt
    to_ans = INR_TO_OTHER[to] * in_inr
    return to_ans
