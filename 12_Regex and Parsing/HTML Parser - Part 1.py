# python 2.x
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for attr in attrs:
            print "-> %s > %s" % (attr[0], attr[1])
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for attr in attrs:
            print "-> %s > %s" % (attr[0], attr[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
html = ""
for _ in range(int(raw_input())):
    html += raw_input()
parser.feed(html)