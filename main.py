from flask import Flask

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def form_sample(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1 class="alert alert-primary" role="alert"> Мое предложение: {planet_name.capitalize()}
                        <h2 class="alert alert-secondary" role="alert"> Эта земля близка к Земле:; </h2>
                        <h2 class="alert alert-success" role="alert"> На ней много необходимых ресурсов; </h2>
                        <h2 class="alert alert-danger" role="alert"> На ней есть небольшое 
                        магнитное поле; </h2>
                        <h2 class="alert alert-warning" role="alert"> Наконец, она просто 
                        красивая; </h2>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
