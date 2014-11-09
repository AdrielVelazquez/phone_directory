import os
import socket
import sys
import re

from couchapp import commands
from couchapp.config import Config
import couchdb

RE_COUCH_URL = re.compile(r'^(https?)://(([_a-zA-Z0-9-]+):(.+)@)?(([a-zA-Z0-9\.-]+)(:([0-9]+))?)/([_a-zA-Z0-9-]+)/?$')

def parse_couchdb_url(s):
    """returns tuple (scheme, user, pass, host, port, dbname) or False

    user, pass & port may be returned as empty strings if not present

    >>> parse_couchdb_url("http://localhost:5984/db")
    ('http', '', '', 'localhost', '5984', 'db')
    >>> parse_couchdb_url("http://localhost:5984/db-name")
    ('http', '', '', 'localhost', '5984', 'db-name')
    >>> parse_couchdb_url("http://localhost:5984/db_name")
    ('http', '', '', 'localhost', '5984', 'db_name')
    >>> parse_couchdb_url("http://127.0.0.1:5984/db_name")
    ('http', '', '', '127.0.0.1', '5984', 'db_name')
    >>> parse_couchdb_url("http://127.0.0.1/db_name")
    ('http', '', '', '127.0.0.1', '', 'db_name')
    >>> parse_couchdb_url("https://127.0.0.1:5984/db_name")
    ('https', '', '', '127.0.0.1', '5984', 'db_name')
    >>> parse_couchdb_url("https://user:pass@127.0.0.1:5984/db_name")
    ('https', 'user', 'pass', '127.0.0.1', '5984', 'db_name')
    >>> parse_couchdb_url("https://us-er:pa-ss@127.0.0.1:5984/db_name")
    ('https', 'us-er', 'pa-ss', '127.0.0.1', '5984', 'db_name')
    >>> parse_couchdb_url("https://us-er:pa-ss@127.0.0.1/db_name/")
    ('https', 'us-er', 'pa-ss', '127.0.0.1', '', 'db_name')

    """


    match = RE_COUCH_URL.match(s)
    if match:
        m = match.groups()
        # ('https', 'user:pass@', 'user', 'pass', '127.0.0.1:5984',
        # '127.0.0.1', ':5984', '5984', 'db_name')
        scheme = m[0]
        usr = m[2] or ''
        pwd = m[3] or ''
        host = m[5]
        port = m[7] or ''
        dbname = m[8]
        return (scheme, usr, pwd, host, port, dbname)
    return False

def usage():
    """returns usage message as string"""
def usage():
    """returns usage message as string"""
    ex_url = "scheme://username:password@server/dbanme"

    return '''push design doc to server

usage:

    {} SERVER_URL DESIGN_DIR

example:

    {} {} ./db/number-db/designs/numbers

'''.format(sys.argv[0], sys.argv[0], ex_url)

if '-h' in sys.argv or '--help' in sys.argv:
    print >> sys.stdout, usage()
    sys.exit(0)
if len(sys.argv) < 3:
    print >> sys.stderr, usage()
    sys.exit(1)

server_url = sys.argv[1]
real_url = server_url
design_dir = sys.argv[2]


try:
    (scheme, user, pwd, host, port, dbname) = parse_couchdb_url(server_url)
except TypeError:
    raise RuntimeError("Could not parse url %s" % (server_url, ))

if "localhost" not in host.lower() and scheme.lower() != "https":
    raise RuntimeError("Insecure HTTP, add HTTPS")

if port:
    host = "%s:%s" % (host, port)
server_url = "%s://%s" % (scheme, host)



server = couchdb.Server(server_url)
if user and pwd:
    server.resource.credentials = (user, pwd)

try:
    print >> sys.stderr, "server connection test...", 
    print >> sys.stderr, "found version %s" % (server.version(), )
except socket.error:
    print >> sys.stderr, ""
    raise RuntimeError("could not connect to %s" % (server_url, ))

try:
    db = server[dbname]
except couchdb.http.ResourceNotFound:
    raise RuntimeError("no db %s on %s" % (dbname, server_url))

(design_path, design_name) = design_dir.rsplit('/', 1)
os.chdir(design_path)

print >> sys.stderr, "Pushing {} to {}".format(design_name, host),
commands.push(Config(), design_name, real_url)


sys.exit(0)
