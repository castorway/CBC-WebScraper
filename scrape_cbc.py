from io import StringIO
import requests
from bs4 import BeautifulSoup
import sys

class Parser():
    def __init__(self, url, output_to=None):

        if type(output_to) == str:
            self.out = open(output_to, "w")
            self.output_to_file = True
        else:
            self.out = None
            self.output_to_file = False

        self.url = url

    def __del__(self):
        print("parser deleted...")
        if self.output_to_file:
            self.out.close()

    def output(self, txt):
        if self.output_to_file:
            self.out.write(txt)
        else:
            print(txt)
    
    def parse(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'html.parser')

        # get title
        self.output("TITLE: " + soup.h1.string)

        # get author
        author_block = soup.find_all(class_='authorText')[0].a
        self.output("AUTHOR: " + author_block.text)
        self.output("-> Author link: " + "https://www.cbc.ca" + author_block['href'])

        # get date
        self.output("POSTED: " + soup.time['datetime'][:10])

        # get body text
        story = soup.find_all(class_="story")[0].span

        for tag in story.children:
            if tag.name == 'h2':
                self.output('--' + tag.text + '--')
            if tag.name == 'p':
                self.output(tag.text)

if __name__ == "__main__":
    # TODO input validation

    url = sys.argv[1]

    if len(sys.argv) > 2:
        output_to = open(sys.argv[2], "w")
    else:
        output_to = sys.stdout

    with open("out.txt", "w") as f:
        parser = Parser(url, f)
    parser.parse()