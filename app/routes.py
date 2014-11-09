from flask import Blueprint, request

from tools.phone_numbers import get_random_start_n, get_random_other_digits

quiz = Blueprint('SET', __name__, url_prefix='/SET')


@quiz.route("/number", methods=['GET'])
def get_number():
    '''
    Requests a new number from couchdb
    '''
    print request.args
    number = get_random_start_n()
    return {"number": number}