from connections import server_connection

def check_database(db_name):
    """
    Verify that the database is a test database.
    """
    if not db_name.startswith("test"):
        print "YIKES DATABASE '{database}' IS NOT A TEST DATABASE! EXITING!".format(database=db_name)
        exit()

def setup_database(db_name):
    check_database(db_name)
    server = server_connection()

    try:
        server.delete(db_name)
    except:
        pass

    server.create(db_name)


def tear_down_database(db_name, delete=True,
                       verbose=True):
    check_database(db_name)
    server = server_connection()
    if delete:
        if verbose:
            print "    Deleting database {database}...".format(database=db_name)
        server.delete(db_name)