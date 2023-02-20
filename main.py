from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        "title": "Auto Answer",
        "Surname": "Kosov",
        "Name": "Mikhail",
        "Education": "Middle",
        "Profession": "Coder",
        "Sex": "Male",
        "Motivation": "Earn to much money",
        "Ready": "Yes"
    }
    return render_template("auto_answer.html", **data)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
