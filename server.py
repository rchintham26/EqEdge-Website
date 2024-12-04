from flask import Flask, render_template, request
from ticker import get_price
from waitress import serve



app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/ticker')
def get_ticker():
    data = get_price(request.args.get('ticker'))
    return render_template(
        'ticker.html',
        title = 'Ticker Value',
        status = 'success',
        ticker = request.args.get('ticker'),
        data = data
    )

if __name__ == '__main__':
    serve(app,host="0.0.0.0",port=8000)

