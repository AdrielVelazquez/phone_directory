from flask import Blueprint, request

from tools.phone_numbers import get_custom_number, get_phone_numbers_by_user, get_phone_number_v2, unassign_number

quiz = Blueprint('SET', __name__, url_prefix='/SET')


@quiz.route("/number", methods=['GET'])
def get_number():
    '''
    Requests a new number from couchdb
    '''
    user = request.args.get("user")
    custom_number = request.args.get("number")
    if not user:
        return {"error": "Must give a user argument in the number request ?user=Adriel"}
    if custom_number:
        return get_custom_number(user, custom_number)
    number = get_phone_number_v2(user=user)
    return {"number": number}

@quiz.route("/assigned", methods=['GET'])
def get_user_numbers():
    '''
    gets a list of all numbers assigned to one user
    '''
    user = request.args.get("user")
    if not user:
        return {"error": "Must give a user argument in the assigned request ?user=Adriel"}
    numbers = get_phone_numbers_by_user(user=user)
    return {"numbers": numbers}


@quiz.route("/unassign", methods=['GET'])
def unassign():
    '''
    Requests a new number from couchdb
    '''
    number = request.args.get("number")
    if not number or len(number) != 10 or number.isdigit() is False:
        return {"error": "Must give a number argument in the assigned request ?number=2342342345"}
    details = unassign_number(number)
    return details