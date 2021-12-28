# CBC-WebScraper
A web scraper that parses a [CBC](https://www.cbc.ca/) article to the command line or a file.

This is an open source project from [DevProjects](http://www.codementor.io/projects), made for an AlbertaSat Ground-Station Software kickoff project.

## Tech/framework used
- Python3
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://docs.python-requests.org/en/master/)

## Dependencies
Requires Python libraries beautifulsoup4 and Requests to be installed.

`pip install bs4`

`pip install requests`

## Usage
`scrape_cbc.py` takes a required 'URL' argument and an optional 'location' argument.

`python3 scrape_cbc.py <url> <location>`

The 'location' argument can be the name of a file (which will be overwritten) to print the parsed webpage to. If left empty, the parsed page will be printed to the command line.

Example usage:

`python3 scrape_cbc.py https://www.cbc.ca/news/canada/saskatoon/saskatchewan-extreme-cold-weather-1.6298814 parsed_article.txt`
