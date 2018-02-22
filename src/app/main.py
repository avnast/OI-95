from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    d = request.values.get('d', '')
    msg = ''
    h = ''
    b = ''
    if d != '':
        try:
            h = hex(long(d))
            b = bin(long(d))
        except:
            msg = 'Please enter valid decimal number'
            
    return render_template('index.html', d=d, h=h, b=b, msg=msg)

