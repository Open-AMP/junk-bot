from __future__ import print_function
import json
import requests
from pprint import pprint
import sys
import pymongo
import getpass


def log(msg):
    print(msg, file=sys.stderr)

def inline_log(msg):
    print(msg, end='', file=sys.stderr)

def put_junk_to_db(file_name, root):
    log('parse file : %s' % file_name)
    log('loading file......')
    # This needs to be complete
    # Firstly Pull coverage from 
    # puppeteer and parse the json file 
    # and push to mlab
    API_KEY = 'mS7qtU5uAY2Lza7A2mGHieDVEfE8AfLs'
    api_url = 'https://api.mlab.com/api/1/databases/junkbot/collections/css?apiKey=%s' % API_KEY
    return requests.post() # need to complete

# execution starts here
if __name__ == '__main__':
    response = put_junk_to_db('wikipedia-CSSCoverage.json', 'https://en.wikipedia.org/wiki/Main_Page')
    if response.status_code == 200:
        log('successfully inserted into the database')
    else:
        log('some error occurred while inserting to database')

