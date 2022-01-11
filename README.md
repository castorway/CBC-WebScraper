# CBC-WebScraper
A web scraper that parses a [CBC](https://www.cbc.ca/) article to the command line or a file.

This is an open source project from [DevProjects](http://www.codementor.io/projects), made for an AlbertaSat Ground-Station Software kickoff project.

## Dependencies
Requires Python libraries [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) and [Requests](https://docs.python-requests.org/en/master/) to be installed.

`pip install bs4`

`pip install requests`

## Usage
`scrape_cbc.py` takes a required 'URL' argument and an optional 'location' argument.

`python3 scrape_cbc.py <url> [-n filename] [-f format]`

The 'filename' argument can be the name of a file (which will be overwritten) to print the parsed webpage to. If left empty, the parsed page will be printed to the command line.

The 'format' argument can be one of 'format' (default), 'keep', and 'skip'.
* 'skip' causes the h2 subtitle lines to be skipped
* 'keep' causes them to be printed like normal paragraph text
* 'format' causes them to be printed in all-caps for readability

Example usage:

`python3 scrape_cbc.py https://www.cbc.ca/news/canada/saskatoon/saskatchewan-extreme-cold-weather-1.6298814 -n parsed_article.txt -f skip`
