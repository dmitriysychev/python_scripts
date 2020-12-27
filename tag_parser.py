from bs4 import BeautifulSoup
import urllib.request as request
import urllib.error as err

# In Python there is a feature for simple print style debugging to be switched on or off.
# If you run a Python script with the -O option then
# python -O habr.py means run with debug == false
class Parser:

    def __init__(self, website):
        self.website = website
    
    def __str__(self):
        return f"Parser of the website: {self.website}"

    # strict type specialization
    def getSoup(self, link: str):
        response = None
        try:
            response = request.urlopen(link)
        except err.URLError as re:
            raise re

        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    '''
    # Method for parsing
    # returns a list of tags specified by the parameter 'html_tag'
    '''
    def parse(self, soup, html_tag, class_name = None):
        attrs = {}
        self.tags = []
        if class_name is not None:
            attrs = {'class': class_name}
            
        for tag in soup.findAll(html_tag, attrs): # tag='article', class_name = 'post post_preview'
            if __debug__: 
                print(tag)
            self.tags.append(tag)
        return self.tags

    '''
    # In order to get what you want from the website, specify *tag* param
    # and *class* param if you want particular class
    '''
    def getListOfTags(self, tag = None, className = None):
        soup = self.getSoup(self.website)
        listOfTags = self.parse(soup, tag, className)
        return listOfTags

    '''
    # Pretty print of the website as a text
    '''
    def ppretty(self):
        print(self.getSoup(self.website).prettify())

    '''
    # Function to extract a specific tag from the
    # list of tags we parsed
    '''
    def extractTag(self, tag, tagList):
        specificTags = []
        [specificTags.append(element.find(tag)) for element in tagList]
        return specificTags

# usage example:
habr = Parser("https://habr.com/en/flows/develop/")
print(habr)
storedTags = habr.getListOfTags('article', 'post post_preview')

particularTagList = habr.extractTag('h2', storedTags)

# for example this is how you would get a post titles from this website
# every title on this website is a link and stored under <a></a> tags
# so if you want to extract a list of titles, perform the following:
print([element.find('a').string for element in particularTagList])