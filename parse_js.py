from __future__ import print_function
import json
import requests
from pprint import pprint
import sys


def log(msg):
	print(msg, file=sys.stderr)

def parse_js(file_name):
	log("parse file : %s"%file_name)
	log("loading file......")
	fhand = open(file_name, 'r')
	j = json.load(fhand)
	fhand.close()
	file = file_name.split(".")[0]
	f = open(file+".txt", "w")
	for result in j.get("result"):
		url = result.get("url")

		if url == '':
			continue

		if url.endswith(".js"):
			log("parsing for url : %s"%url)
			response = requests.get(url).content
			# log(response[608:630])
			# continue
			for function in result.get("functions"):
				for r in function.get("ranges"):
					startOffset = r.get("startOffset")
					endOffset = r.get("endOffset")	
					count = r.get("count")
					if(count != 0):
						continue
					_result = response[startOffset:endOffset]
					f.write(_result + "\n\n")
					log(_result)
					log("")
					log("")
	f.close()

if __name__ == '__main__':
	parse_js("wikipedia-JSCoverage.json")