# HW-WebScraper
This is an open source project from [DevProjects](http://www.codementor.io/projects).

## Tech/framework used
-> Python3
-> BeautifulSoup4
-> Requests

## Dependencies
Requires Python3. Also requires Python libraries BeautifulSoup4 and Requests to be installed.
`pip install requests`
`pip install bs4`

## Usage
`scrape_cbc.py` takes a required `url` argument and an optional `location` argument.
`python3 scrape_cbc.py <url> <location>`
The `location` parameter can be the name of a file (this will be overwritten) to print the parsed webpage to. If left empty, the parsed page will be printed to the command line.

Example usage:
`python3 scrape_cbc.py https://www.cbc.ca/news/canada/saskatoon/saskatchewan-extreme-cold-weather-1.6298814 parsed_article.txt`