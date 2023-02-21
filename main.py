from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    data = [str(i) for i in range(2, 10)]
    return render_template('by_cabins.html', data=data)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
