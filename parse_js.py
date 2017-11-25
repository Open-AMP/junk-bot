from __future__ import print_function
import json
import requests
from pprint import pprint
import sys


def log(msg):
    print(msg, file=sys.stderr)

def parse_js(file_name):
    log('parse file : %s' % file_name)
    log('loading file......')
    json_data = json.load(open(file_name, 'r'))
    results = json_data.get('result')
    if results is None:
        raise Exception('No results in coverage json')
    store = {}
    # file = file_name.split('.')[0]
    # f = open(file+'.txt', 'w')
    for result in results:
        url = result.get('url')
        if not url or not url.endswith('.js'):  # can fail in certain cases
            continue
        log('parsing for url : %s' % url)
        response = requests.get(url).content
        useless_list = []
        for function in result.get('functions'):
            useless_str = ''
            for _range in function.get('ranges'):
                # start = _range.get('startOffset')
                # end = _range.get('endOffset')    
                # count = _range.get('count')
                # if(count != 0):
                    # continue
                if _range.get('count') == 0:
                    continue
                # _result = response[start:end]
                useless_str += response[_range.get('startOffset'):_range.get('endOffset')] + '\n'
                # f.write(_result + '\n\n')
                # log(_result)
                # log('')
                # log('')
            useless_list.append(useless_str)
        store[url] = useless_list
    # print('store:', store)
    json.dump(store, open('ext_%s.json' % (file_name.split('.')[0]), 'w'))


if __name__ == '__main__':
    parse_js('wikipedia-JSCoverage.json')
