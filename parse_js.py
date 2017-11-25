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
    json_data = json.load(open(file_name, 'r'))
    results = json_data.get('result')
    if results is None:
        raise Exception('No results in coverage json')
    store = []
    for result in results:
        url = result.get('url')
        if not url or not url.endswith('.js'):  # can fail in certain cases
            continue
        log('parsing for url : %s' % url)
        response = requests.get(url).content
        junk_list = []
        for function in result.get('functions'):
            junk_str = ''
            for _range in function.get('ranges'):
                if _range.get('count') == 0:
                    continue
                cur_str = response[_range.get('startOffset'):_range.get('endOffset')] + '\n'
                if len(cur_str) > 10:
                    junk_str += cur_str
                inline_log('.')
            junk_list.append(junk_str)
        log('')
        # store[url] = junk_list
        store.append({
            'file': url,
            'junk_length': len(junk_list),
            'junk_list': junk_list
            })

    db_obj = {
        'type': 'js-junk',
        'root': root,
        'junk': store
    }
    API_KEY = 'mS7qtU5uAY2Lza7A2mGHieDVEfE8AfLs'
    api_url = 'https://api.mlab.com/api/1/databases/junkbot/collections/js?apiKey=%s' % API_KEY
    # connection = pymongo.MongoClient('ds121456.mlab.com', 21456)
    # db = connection.junkbot
    # db.authenticate('junkbot', getpass.getpass())
    # js = db.js
    # js.insert_one(db_obj)
    return requests.post(api_url, data=json.dumps(db_obj), headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    response = put_junk_to_db('wikipedia-JSCoverage.json', 'https://en.wikipedia.org/wiki/Main_Page')
    if response.status_code == 200:
        log('successfully inserted into the database')
    else:
        log('some error occurred while inserting to database')

