from flask import Flask

app = Flask(__name__)

@app.route('/list/<path:args>')
def sum_and_multi(args):




if __name__ == '__main__':
    app.run(debug=True, port=1111)
