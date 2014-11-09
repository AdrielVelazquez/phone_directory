from app.models.number_model import get_phone_model
from connections import get_numbers_db


def bulk_load(db, doc_list):
    db.update(doc_list)
    return True


def generate_all_phone_number_combinations():
    '''
    In a real scenario, I'll have the database ingest all possible number combinations,
    This will allow for all numbers to be given a digit before hand.
    Also, I only placed the area code until 201, for testing purposes
    '''
    list_of_numbers = []
    ndb = get_numbers_db()
    for area in range(200, 1000):
        for num in range(2000000, 10000000):
            doc = get_phone_model()
            doc['_id'] = str(area) + str(num)
            doc["assigned"] = False
            list_of_numbers.append(doc)
            print doc["_id"]
            if len(list_of_numbers) == 200:
                print "Saving Batch"
                bulk_load(ndb, list_of_numbers)
                list_of_numbers = []
    bulk_load(ndb, list_of_numbers)

if __name__ == "__main__":
    generate_all_phone_number_combinations()