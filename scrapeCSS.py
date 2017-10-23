from __future__ import print_function
import sys
import requests
from pprint import pprint
from bs4 import BeautifulSoup as Soup
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', nargs='+', help='url to fetch css')
args = parser.parse_args()

try:
    fhandle = open('junk_bot.pickle', 'rb')
    Store = pickle.load(fhandle)
except:
    Store = {}

''' structures of the Store
Store = {
    url: {
        'css_urls': [],
        'css_strings': { 'css_url': 'string'}
    }
}
'''
if args.url:
    url_list = args.url
else:
    print('No url specified, screw you!!!')
    sys.exit(1)

def log(msg):
    print(msg, file=sys.stderr)

def css_list(url):
    ''' takes url of the website and returns a list of css urls'''
    log('fetching html data...')
    html_data = requests.get(url).content
    log('creating soup...')
    soup = Soup(html_data, 'html.parser')
    link_tags = soup.findAll('link', attrs={'rel': 'stylesheet'})
    log('%d link tags found!'%len(link_tags))
    css_link_list = []
    for link in link_tags:
        if '.css' in link.get('href'):
            css_link_list.append(link.get('href'))
    return css_link_list


def save_to_store(url):
    ''' takes a url of the website and saves css details into store '''
    css_link_list = css_list(url)
    log('%d css files found!'%len(css_link_list))
    log('Here\'s css links list: %s' % str(css_link_list))
    if not Store.get(url): Store[url] = {}
    Store[url]['css_urls'] = css_link_list
    log('storing css_content to store...')
    for css_url in css_link_list:
        css_content = requests.get(css_url).content
        css_content = css_content[:200] + ' ..................'
        if not Store[url].get('css_strings'):
            Store[url]['css_strings'] = {}
        Store[url]['css_strings'][css_url] = css_content
    log('done!!!')

if __name__ == '__main__':
    for url in url_list:
        try:
            save_to_store(url)
        except requests.exceptions.ConnectionError:
            print("Please check your internet connection")
    fhandle = open('junk_bot.pickle', 'w')
    pickle.dump(Store, fhandle)
