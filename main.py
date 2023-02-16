from flask import Flask, url_for

app = Flask(__name__)

@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Отбор астронавтов</title>
                      </head>
                      <body>
                        <div>
                            <form class="login_form" method="post">
                                <input type="surname" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Фамилия" name="surname">
                                <input type="name" class="form-control" id="name" placeholder="Имя" name="name">
                                <input type="email" class="form-control" id="email" placeholder="Email" email="email">
                                <div class="form-group">
                                    <label for="classSelect">Образование</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>Начальное</option>
                                      <option>Среднее</option>
                                      <option>Высшее</option>
                                    </select>
                                 </div>
                                <div class="form-group">
                                    <label for="form-check">Выбор основной профессии</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="profession" id="first" value="profession" checked>
                                      <label class="form-check-label" for="first">
                                        Инженер-Исследователь
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="profession" id="second" value="profession" checked>
                                      <label class="form-check-label" for="second">
                                        Инженер-строитель
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="profession" id="third" value="profession" checked>
                                      <label class="form-check-label" for="third">
                                        Пилот
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="profession" id="fourth" value="profession" checked>
                                      <label class="form-check-label" for="fourth">
                                        Метереолорог
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="profession" id="fivth" value="profession" checked>
                                      <label class="form-check-label" for="fivth">
                                        Инженер по жизниобеспечению
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="profession" id="sixth" value="profession" checked>
                                      <label class="form-check-label" for="sixth">
                                        Инженер по радиционной защите
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="profession" id="seventh" value="profession" checked>
                                      <label class="form-check-label" for="seventh">
                                        Врач
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="profession" id="eightth" value="profession" checked>
                                      <label class="form-check-label" for="eightth">
                                        Экзобиолог
                                      </label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label for="about">Мотивация</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')