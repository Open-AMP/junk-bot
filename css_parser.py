import re

def get_object_from_string(css_string):
	pattern = r'(?P<elem>[\w\-]+)\s*\{.*?\}'
	return re.findall(pattern, css_string)