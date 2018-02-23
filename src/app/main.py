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
            h = hex(int(d))[2:]
            o = oct(int(d))[1:]
            b = bin(int(d))[2:]
        except:
            msg = 'Please enter valid decimal number'
            
    return render_template('index.html', d=d, h=h, o=o, b=b, msg=msg)

