from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    a = 0
    b = 0
    c = 0
    if 'a' in request.args:
        a = int(request.args['a'])
    if 'b' in request.args:
        b = int(request.args['b'])
    if 'c' in request.args:
        c = int(request.args['c'])
    summa = a + b + c
    return render_template('hello.html', summa=summa)
app.run(debug=True, port=8080)