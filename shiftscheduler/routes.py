
from calendar import Calendar
from datetime import date, datetime

from flask import Flask, render_template, make_response, jsonify, request

from .config import c
from .cache import Cache


App = Flask(__name__)


# <<- create 6x7 matrix -> week x days
def month_matrix(month: int, year: int, steps: list, start_date: date) -> list:
    """ Helper function for get-help route to get month data paired with shift steps """
    cal = Calendar(6)  # NOTE: from Sun -> Sat
    matrix = list(cal.itermonthdays(year, month))

    # adding shift steps for this the requested month starting with day 1
    diff_days = (date(year, month, 1) - start_date).days

    if diff_days >= 0:
        start_index = diff_days % len(steps)
        steps = [
            steps[(start_index + (x % len(steps))) % len(steps)] for x in range(len(matrix))
        ] + list([None] * 7)
    else:
        start_index = (abs(diff_days) % len(steps)) + 1
        steps = [
            steps[(start_index + (x % len(steps))) % len(steps)] for x in range(len(matrix))
        ]
        #steps = [None] * len(matrix)

    matrix = list(matrix + list([0] * 7))[:42]
    for idx, day in enumerate(matrix):
        if not day:
            matrix[idx] = (day, None, None)
        else:
            _data = Cache.get(f"{year}/{month}/{day}")
            step = steps.pop(0)

            matrix[idx] = (day, _data['step'] or step, bool(_data['note']))

    # NOTE: return a 6x7 list ('weeks' x 'days')
    return [matrix[i:(i + 7)] for i in [(x * 7) for x in range(6)]]
# ->>


@App.route("/")
def index():
    return render_template('index.html')


# <<- '/cache' ["POST", "DELETE"] handle cache requests
@App.route("/cache", methods=['POST', 'DELETE'])
def chaching():
    cli_data = request.get_json()

    if not isinstance(cli_data, dict):
        return make_response("Data format should be a json dict!", 400)

    _date = cli_data.get('date')

    # check date format
    try:
        datetime.strptime(_date, '%Y/%m/%d')
    except ValueError:
        return make_response("Wrong date format, should be: 'YYYY/MM/DD'!", 400)
    except TypeError:
        return make_response("Wrong data format for 'date', should be: a 'string'!", 400)

    _date = str('/'.join(map(str, map(int, _date.split('/')))))  # NOTE: remove 0 from ex: 2021/02/01

    if request.method == 'POST':
        data_to_cache = cli_data.get('data')

        # check data format
        if isinstance(data_to_cache, dict):
            keys_allowed = ['step', 'note']
            for key in data_to_cache:
                if key not in keys_allowed:
                    return make_response(f"Chache key '{key}' not allowed!", 400)
        else:
            return make_response("Data for key 'data' should be a json dict!", 400)

        # store data
        Cache.set(_date, **data_to_cache)

    elif request.method == 'DELETE':
        try:
            Cache.unset(_date)
        except KeyError:
            return make_response(f"No such key: '{_date}'", 400)

    return make_response(jsonify(None), 200)
# ->>


@App.route("/config", methods=['POST'])
def config():
    _config = request.get_json()

    if not isinstance(_config, dict):
        return make_response("Data format should be a json dict!", 400)

    c.ini.read_dict(_config)

    return make_response(jsonify(None), 200)


# <<- '/html/month' ["POST"] generate grid for requested month
@App.route("/html/month", methods=['POST'])
def html_month():
    """ Return grid content for month """
    # get json data: 'year', 'month'
    cli_data = request.get_json()

    if not isinstance(cli_data, dict):
        return make_response("wrong json data", 400)

    if not c.start_date:
        return make_response("missing 'start_date' in configuration", 404)

    year = cli_data.get('year') or datetime.now().year
    month = cli_data.get('month') or datetime.now().month

    return make_response(
        jsonify(
            {
                'html': render_template(
                    'jinja/month.html',
                    month=month_matrix(month, year, c.steps, c.start_date),
                    today=datetime.now().day if f"{datetime.now().year}/{datetime.now().month}" == f"{year}/{month}" else None
                )
            }
        ), 200
    )
# ->>


# <<- '/html/note' ["POST"] generate note popup for the requested day
@App.route("/html/note", methods=['POST'])
def html_note():
    cli_data = request.get_json()

    if not isinstance(cli_data, dict):
        return make_response("Data format should be a json dict!", 400)

    for key in ['step', 'year', 'month', 'day']:
        if key not in cli_data:
            return make_response(f"Missing key in json data: '{key}'", 400)

    note = Cache.get(f"{int(cli_data['year'])}/{int(cli_data['month'])}/{int(cli_data['day'])}")['note']

    return make_response(
        jsonify({
            'html': render_template(
                'jinja/note.html',
                step=cli_data['step'],
                year=cli_data['year'],
                month=cli_data['month'],
                day=cli_data['day'],
                note=note,
                select=list(set(c.steps))
            )
        }), 200
    )
# ->>


@App.route("/html/settings", methods=['GET'])
def html_settings():
    return make_response(
        jsonify({
            'html': render_template(
                'jinja/settings.html',
                config=c.ini.__dict__['_sections']
            )
        }), 200
    )
