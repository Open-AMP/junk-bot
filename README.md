# Junk Bot
---
This Tool aims to identify and reduce code-junk or visually appealing codebase which does not aid user-interaction, first paint / first interactive timing and slows down page loading on slower networks and devices.
--- 

* ScrapeCSS 
	* This script is all about scraping css from various websites.
	* It takes a url of the website, and fetches `html` using requests library. 
	* ```html_data = requests.get(url).content```
	* Then it fetches all the css links using `BeautifulSoup`.
	* Then it again fetches css content using `requests` library.
	* Creates a store dictionary containing details in hierarchical structure.
	* Then it stores the entire store into a file for reusable purposes.
```python
# Structure of store
Store = {
    url: {
        'css_urls': [],
        'css_strings': { 'css_url': 'string'}
    }
}
```

* ScrapeJS
	* Similarly to the CSS script, this scrapes JS from various websites
	* All functionalities are similar to the CSS script
```python
# Structure of store
Store = {
    url: {
        'js_urls': [],
        'js_strings': { 'js_url': 'string'}
    }
}
```
