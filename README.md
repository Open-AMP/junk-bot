# Junk Bot


This Tool aims to identify and reduce code-junk or visually appealing codebase which does not aid user-interaction, first paint / first interactive timing and slows down page loading on slower networks and devices.

## Usage

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
* jsCov
	* This script uses the `V8 code coverage` feature to identify and report unsused `JS` code portions.
	* It takes a `url` for a website and runs a `headless chrome` instance 
	* `Profiler.takePreciseCoverage` is called on this instance using `chrome-debugging-client`
	* This returns a coverage store with `callcount` of each function listed
```javascript
# Coverage Structure
Result = {
"scriptId": String,
"url": String,
"functions": [
	{
    	"functionName": String,
        "ranges": [
        	{
            "startOffSet": Number,
            "endOffSet": Number,
            "count": Number
            }
        ],
        "isBlockCoverage": Boolean
     }
 ]
},
```
* cssCov
	* This script uses the `V8 code coverage` feature to identify and report unsused `CSS` code portions.
	* It takes a `url` for a website and runs a `headless chrome` instance 
	* `CSS.takeCoverageDelta` is called on this instance using `chrome-debugging-client`
	* This returns a coverage store of all unused css portions
```javascript
# Coverage Structure
Coverage = [
	{
    	"index": Number,
        "css": String
    },
```