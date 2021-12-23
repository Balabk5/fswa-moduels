from flask import Flask
from flask import render_template, request


app = Flask(__name__)


@app.route('/home', methods=["GET", "POST"])
def trying():
    if request.method == "POST":
        N_value = request.form.get("N-value")
        K_value = request.form.get("k-value")
        p_value = request.form.get("p-value")
        city = request.form.get("city")
        print(N_value)
        print(K_value)
        print(p_value)
        print(city)
    return render_template("croppred.html")
