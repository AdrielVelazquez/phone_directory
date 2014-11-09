from app.models.number_model import get_phone_model
from connections import get_numbers_db


def bulk_load(db, doc_list):
    db.update(doc_list)
    return True


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
            print doc["_id"]
    return list_of_numbers

if __name__ == "__main__":
    nums = generate_all_phone_number_combinations()
    bulk_load(get_numbers_db(), nums)