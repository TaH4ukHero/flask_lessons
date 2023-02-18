from flask import Flask

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def form_sample(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1 class="alert alert-primary" role="alert"> Мое предложение: Результаты 
                        отбора </h1>
                        <h2 class="alert alert-secondary" role="alert"> Претендента на участие в 
                        миссии {nickname} </h2>
                        <h2 class="alert alert-success" role="alert"> Поздравляем! Ваш рейтинг 
                        после {level} этапа отбора 
                        </h2>
                        <h2 class="alert alert-danger" role="alert"> Составляет {rating}</h2>
                        <h2 class="alert alert-warning" role="alert"> Желаем удачи </h2>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
