import json

import connections
from app.models.number_model import get_phone_model

def bulk_load(db, doc_list):
    db.update(doc_list)
    return True


def load_codes():
    '''
    The data from the zips is being pulled from a json file I extracted from a website,
    Th data will instead
    '''
    json_data = open('area.json', "r")
    data = json.load(json_data)
    area_dict = {"_id": "area_codes"}
    for key, value in data.iteritems():
        key = str(key)
        value = str(value).lower()
        if value == "--":
            value = "any"
        if value in area_dict:
            area_dict[value].append(key)
        else:
            area_dict[value] = [key]

    return area_dict

def generate_all_phone_number_combinations():
    '''
    In a real scenario, I'll have the database ingest all possible number combinations,
    This will allow for all numbers to be given a digit before hand.
    '''
    list_of_numbers = []
    for area in range(200, 999):
        for num in range(2000000, 9999999):
            doc = get_phone_model()
            doc['_id'] = str(num) + str()
            doc["assigned"] = False
            list_of_numbers.append(doc)
    bulk_load(connections.get_numbers_db(), list_of_numbers)

if __name__ == "__main__":
    ndb = connections.get_numbers_db()
    area_codes_doc = load_codes()
    result = bulk_load(db=ndb, doc_list=[area_codes_doc])




