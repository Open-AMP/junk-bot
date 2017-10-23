# Junk Bot

* ScrapeCSS 
	* This script is all about scraping css from various websites.
	* It takes a url of the website, and fetches `html` using requests library. 
	* ```html_data = requests.get(url).content```
	* Then it fetches all the css links using `BeautifulSoup`.
	* Then it again fetches css content using `requests` library.
	* Creates a store dictionary containing details in hierarchical structure.
	* ```python
Store = {
    url: {
        'css_urls': [],
        'css_strings': { 'css_url': 'string'}
    }
}
```
	* Then it stores the entire store into a file for reusable purposes.
