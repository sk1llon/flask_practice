from flask import Flask, request
from typing import List

app = Flask(__name__)


@app.route('/list/', methods=['GET'])
def sum_and_multi():
    number_list_a: List[int] = request.args.getlist('numA', int)
    number_list_b: List[int] = request.args.getlist('numB', int)
    return 'Сумма чисел в массиве A: {sum_a}\n' \
           'Сумма чисел в массиве B: {sum_b}\n'.format(
            sum_a=sum(number_list_a),
            sum_b=sum(number_list_b)
            )


if __name__ == '__main__':
    app.run(debug=True, port=1111)

# http://localhost:1111/list/?numA=5&numA=2&numA=1&numA=6&numB=6&numB=2&numB=1&numB=5
