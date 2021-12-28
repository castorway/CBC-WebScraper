import requests
from bs4 import BeautifulSoup
import sys

class Parser():
    def __init__(self, output_to=None, titles='format'):
        """
        `titles` has 3 options: 'skip', 'keep', 'format'.
        -> 'skip' causes the h2 subtitle lines to be skipped
        -> 'keep' causes them to be printed in the parsed text like normal
            paragraph text
        -> 'format' causes them to be printed in all-caps for readability
        """

        if type(output_to) == str:
            self.out = open(output_to, "w")
            self.output_to_file = True
        else:
            self.out = None
            self.output_to_file = False
    
        self.url = url
        self.titles = titles

    def __del__(self):
        """
        Closes file if one was opened for output.
        """
        if self.output_to_file:
            self.out.close()

    def output(self, txt):
        """
        Either prints text to STDOUT or writes it to the file opened when
        the Parser was initialized.
        """
        if self.output_to_file:
            self.out.write(txt + '\n')
        else:
            print(txt)

    def safe_find(self, soup, name=None, attrs={}):
        if name:
            found_tags = soup.find_all(name, attrs=attrs)
        else:
            found_tags = soup.find_all(attrs=attrs)

        if len(found_tags) == 0:
            return False
        else:
            return found_tags[0]

    def parse(self, url):
        """
        Parses the webpage at `url`, assuming it is a typical CBC News article
        page. Outputs using output() function to designated location.
        """
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'html.parser')

        # get title
        title = self.safe_find(soup, name="h1")
        if title:
            self.output("TITLE: " + title.string)
        else:
            self.output("TITLE: [Not Found]")

        # get byline/subtitle
        # when using dictionary for attrs in find_all, BeautifulSoup doesn't
        # require `class_` workaround
        byline = self.safe_find(soup, attrs={"class": "deck"})
        if byline:
            self.output("SUBTITLE: " + byline.text)
        else: 
            self.output("SUBTITLE: [Not Found]")

        # get author
        author = self.safe_find(soup, attrs={"class": "authorText"})
        if author: # some articles don't have an author listed
            self.output("AUTHOR: " + author.text)
        else:
            self.output("AUTHOR: [Not Found]")

        # get date
        date = self.safe_find(soup, name="time")
        if date:
            self.output("DATE: " + date['datetime'][:10])
        else:
            self.output("DATE: [Not Found]")

        self.output("---------------") # divider for readability

        # get body text
        story = self.safe_find(soup, attrs={"class" : "story"})
        if not story:
            self.output("Story text not found.")
            return

        # body text is stored in a span inside the story tag
        story = self.safe_find(story, name="span")
        if not story:
            self.output("Story text not found.")
            return
            
        for tag in story.children:
            if tag.name == 'h2':
                if self.titles == 'format':
                    self.output(tag.text.upper())
                elif self.titles == "keep":
                    self.output(tag.text)
            if tag.name == 'p':
                self.output(tag.text)


def main():
    # input validation. does several checks to decrease likelihood that link
    # is incompatible with parser code.

    url = sys.argv[1]
    valid = True

    if not url.startswith("https://www.cbc.ca/news/"):
        valid = False

    try:
        float(url[-10:])
    except ValueError:
        valid = False
    
    if not valid:
        print("Please use the full URL for a CBC News article.")
        print("Example: https://www.cbc.ca/news/world/coronavirus-covid19-canada-world-dec27-2021-1.6298702")
        sys.exit()

    # checks if a file was provided in input
    if len(sys.argv) > 2:
        output_to = sys.argv[2]
    else:
        output_to = None

    # parses file and prints to output location
    parser = Parser(output_to=output_to, titles="format")
    parser.parse(url)


if __name__ == "__main__":
    main()