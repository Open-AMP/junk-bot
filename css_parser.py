import re

def get_object_from_string(css_string):
	'''this script is to fetch html elements 
	from css file and inline style tags'''
	pattern = r'(?P<elem>[\w\-]+)\s*\{.*?\}'
	return re.findall(pattern, css_string)