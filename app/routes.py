from flask import Blueprint, request

from tools.phone_numbers import get_phone_number

quiz = Blueprint('SET', __name__, url_prefix='/SET')


@quiz.route("/number", methods=['GET'])
def get_number():
    '''
    Requests a new number from couchdb
    '''
    user = request.args.get("user")
    if not user:
        return {"error": "Must give a user argument in the request ?user=Adriel"}
    number = get_phone_number(user=user)
    return {"number": number}