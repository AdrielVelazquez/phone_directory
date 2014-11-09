import random

from connections import get_numbers_db
from app.models import number_model


def get_random_start_n():
    return str(random.randrange(2, 10))


def get_random_other_digits():
    return str(random.randrange(0, 10))


def get_area_code():
    area = []
    while len(area) < 3:
        if not area:
            area.append(get_random_start_n())
            continue
        area.append(get_random_other_digits())

    return "".join(area)

def get_phone_number(user):
    '''
    the convention is:
    NPA-NXX-XXXX

    NPA is the number plan area. Area code. the first digit is always a 2 thru 9
    NXX is the central office. the firstdigit is always 2-9
    XXXX can be any digit
    '''

    phone_number = []
    db = get_numbers_db()
    found_number = False
    while not found_number:
        while len(phone_number) < 7:
            if not phone_number:
                phone_number.append(get_random_start_n())
                continue
            phone_number.append(get_random_other_digits())
        number = get_area_code() + "".join(phone_number)
        doc = db.get(number)

        if not doc:
            doc = number_model.get_phone_model()
            doc['user'] = user
            doc['_id'] = number
            found_number = True
        if not doc.get("assigned"):
            doc['assigned'] = True
            doc['user'] = user
            found_number = True
    db.save(doc)
    return number


def get_phone_number_v2(user):
    db = get_numbers_db()
    number_doc = db.view("numbers/aproved_phone_numbers",
                     startkey=[False], endkey=[False, {}], limit=1).rows[0].value

    number_doc["assigned"] = True
    number_doc["user"] = user
    db.save(number_doc)
    return number_doc["_id"]

def get_custom_number(user, custom_number):
    db = get_numbers_db()
    if int(custom_number[0]) < 2:
        return {"error": "Phone number is an invalid format area code is invalid"}
    elif int(custom_number[3]) < 2:
        return {"error": "Phone number is an invalid format main number is incorrect"}
    elif len(custom_number) != 10:
        return {"error": "Phone number is an invalid format length is less than 10"}
    elif custom_number.isdigit() is False:
        return {"error": "Phone number is not all digits"}
    doc = db.get(custom_number)
    if doc["assigned"]:
        return {"error": "Number already taken, leave number argument blank and random available will be assigned"}
    else:
        doc["user"] = user
        doc["assigned"] = True
        db.save(doc)
        return {"number": custom_number}

def get_phone_numbers_by_user(user):
    db = get_numbers_db()
    rows = db.view("users/number_by_user", startkey=user, endkey=user)
    numbers = []
    for row in rows:
        numbers.append(row.value)
    return numbers

def unassign_number(number):
    db = get_numbers_db()
    doc = db.get(number)

    if not doc or doc["assigned"] is False:
        return {"Warning": "Phone number is already unassigned"}

    doc["assigned"] = False
    doc["user"] = None
    db.save(doc)

    return {"Info": "Successfully unassigned number ".format(number)}