from flask import Flask, render_template, request

app = Flask(__name__)

ncopy = "copyriht © 2024 raflynurihvandi"
@app.route("/")
def home():
    return render_template('home.html', ncopy = ncopy)

@app.route("/kalkulator", methods=['GET', 'POST'])
def abou():
    if request.method == 'POST':
        ap = int(request.form['angka_pertama'])
        ak = int(request.form['angka_kedua'])
        op = request.form['operator']
        if op == '+':
            hsl = ap + ak
            return render_template('kalkulator.html', hsl=hsl)
        elif op == '-':
            hsl = ap - ak
            return render_template('kalkulator.html', hsl=hsl)
        elif op == 'x':
            hsl = ap * ak
            return render_template('kalkulator.html', hsl=hsl)
        elif op == '/':
            hsl = ap / ak
            return render_template('kalkulator.html', hsl=hsl, ncopy=ncopy)
    return render_template('kalkulator.html', hsl=None, ncopy=ncopy)

@app.route("/pengalihan")
def pengalihan():
    return render_template('pengalihan.html', ncopy = ncopy)