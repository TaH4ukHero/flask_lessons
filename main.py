from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<value>')
def training(value):
    return render_template('list_prof.html', value=value)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
