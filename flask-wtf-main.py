# WEB. Введение во flask. Обработка HTML-форм
import json
import os

from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename

from forms.gallery import UploadForm
from forms.login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/<title>')
@app.route('/index/<title>')
def index(title=''):
    params = {"title": title}
    return render_template('base.html', **params)


@app.route("/training/<prof>")
def training(prof):
    """
    Тренировки в полёте
    """
    params = {"title": "Тренировки в полёте",
              "prof": prof}
    return render_template('training.html', **params)


@app.route("/list_prof/<lst>")
def list_prof(lst):
    """
    Список профессий
    """
    params = {'title': 'Список профессий',
              'lst': lst,
              'professions': ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                              'инженер по терраформированию', 'климатолог',
                              'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                              'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                              'штурман', 'пилот дронов']}
    return render_template('list_prof.html', **params)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    """
    Автоматический ответ
    """
    params = {'title': 'Анкета',
              'surname': 'Watny',
              'name': 'Mark',
              'education': 'выше среднего',
              'profession': 'штурман марсохода',
              'sex': 'male',
              'motivation': 'Всегда мечтал застрять на Марсе!',
              'ready': 'True'}
    return render_template('auto_answer.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Двойная защита
    login.html простая форма с обходом цикла
    login2.html форма с контролем каждого поля
    """
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login2.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    """
    По каютам!
    """
    params = {'title': 'По каютам!',
              'astronauts': ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                             'Венката Капур', 'Тедди Сандерс', 'Шон Бин']}
    return render_template('distribution.html', **params)


@app.route('/table/<sex>/<int:age>')
def table(sex: str, age: int):
    """
    Цвет каюты
    :param sex: str
    :param age: int
    :return: None
    """
    params = {'title': 'Цвет каюты',
              'sex': sex,
              'age': age}
    return render_template('cabin_color.html', **params)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    """
    Галерея с загрузкой
    :return: None
    """
    form = UploadForm()
    pictures = os.listdir('static/img')
    if form.validate_on_submit():
        filename = secure_filename(form.image_data.data.filename)
        form.image_data.data.save('static/img/' + filename)
        pictures = os.listdir('static/img')
    return render_template('gallery.html', pictures=pictures, title='Галерея с загрузкой', form=form)


@app.route('/member')
def member():
    """
    Личная карточка
    :return: None
    """
    with open('templates/members.json', mode='rt') as file:
        members = json.load(file)
    print(members)
    return render_template('member.html', members=members, title='Личная карточка')


if __name__ == '__main__':
    app.run(port="8080", host="127.0.0.1")
