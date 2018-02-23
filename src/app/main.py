from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    d = request.values.get('d', '')
    msg = ''
    h = ''
    o = ''
    b = ''
    if d != '':
        try:
            h = hex(long(d))
            o = oct(long(d))
            b = bin(long(d))
        except:
            msg = 'Please enter valid decimal number'
            
    return render_template('index.html', d=d, h=h, o=o, b=b, msg=msg)

