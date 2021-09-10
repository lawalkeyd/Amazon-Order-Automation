from flask import Flask

app = Flask(__name__)

@app.route('/kk')
def order():
    return 'Hello BABA'


