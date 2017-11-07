from __future__ import print_function
import sys
import requests
from pprint import pprint
from bs4 import BeautifulSoup as Soup
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', nargs='+', help='url to fetch js')
args = parser.parse_args()

try:
    fhandle = open('junk_bot.pickle', 'rb')
    Store = pickle.load(fhandle)
except:
    Store = {}

if args.url:
    url_list = args.url
else:
    print('No url specified, screw you!!!')
    sys.exit(1)

def log(msg):
    print(msg, file=sys.stderr)

def js_list(url):
    ''' takes url of the website and returns a list of js urls'''
    log('fetching html data...')
    html_data = requests.get(url).content
    log('creating soup...')
    soup = Soup(html_data, 'html.parser')
    link_tags = soup.findAll('script')
    log('%d javascript script tags found!'%len(link_tags))
    js_link_list = []
    js_strings = []
    for link in link_tags:
        if link.string :
            # log(link.string)
            js_strings.append(link.string)
        else:
            if link.get('src') != None:
                js_link_list.append(link.get('src'))
    return (js_link_list, js_strings)


def save_to_store(url):
    ''' takes a url of the website and saves js details into store '''
    js_link_list, js_strings = js_list(url)
    log("%d js strings found" % len(js_strings))
    log('%d js files found!'%len(js_link_list))
    log('Here\'s js links list: %s' % str(js_link_list))
    
    if not Store.get(url): Store[url] = {}
    Store[url]['js_urls'] = js_link_list

    # js_in_string: list of javascript code inside the <script> in html
    Store[url]['js_in_string'] = js_strings
    log('storing js_content to store...')
    for js_url in js_link_list:
        js_content = requests.get(js_url).content
        js_content = js_content[:200] + ' ..................'
        if not Store[url].get('js_strings'):
            Store[url]['js_strings'] = {}
        Store[url]['js_strings'][js_url] = js_content
    log('done!!!')

if __name__ == '__main__':
    for url in url_list:
        try:
            save_to_store(url)
        except requests.exceptions.ConnectionError:
            print("Please check your internet connection")
    fhandle = open('junk_bot.pickle', 'w')
    pickle.dump(Store, fhandle)
