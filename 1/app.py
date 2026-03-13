from flask import Flask
from random import choice
from datetime import datetime, timedelta


app = Flask(__name__)

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']

cats_str = 'корниш-рекс, русская голубая, шотландская вислоухая, мейн-кун, манчкин'
cats = cats_str.split(',')


@app.route('/main')
def main_window():
    return 'Тестовый '


@app.route('/cars')
def get_cars():
    return ', '.join(cars)


@app.route('/cats')
def get_cat():
    return choice(cats)


@app.route('/time')
def current_time():
    return 'Текущие дата и время: {time}'.format(time=datetime.now())


@app.route('/future')
def future_time():
    delta = timedelta(hours=1)
    return 'Время через час: {time}'.format(time=datetime.now() + delta)


@app.route('/counter')
def counter():
    counter.visits += 1
    return str(counter.visits)


counter.visits = 0


@app.route('/compare/<num_1>/<num_2>')
def compare(num_1, num_2):
    if num_1 > num_2:
        return 'Число {} больше числа {}'.format(num_1, num_2)
    elif num_1 < num_2:
        return 'Число {} меньше числа {}'.format(num_1, num_2)
    elif num_1 == num_2:
        return 'Числа равны'
    else:
        return 'Сосни'


@app.route('/max/<path:sequence>')
def max_num(sequence):
    sequence_list = sequence.split('/')
    int_list = list()
    for num in sequence_list:
        if num.isdigit():
            int_list.append(int(num))
    number = max(int_list)
    status_code = 200 if number else 404
    return 'Максимальное число - {num}'.format(num=number), status_code


if __name__ == '__main__':
    app.run(debug=True, port=1111)
