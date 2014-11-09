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