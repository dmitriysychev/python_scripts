from bs4 import BeautifulSoup
import urllib.request as request
import urllib.error as err

# In Python there is a feature for simple print style debugging to be switched on or off.
# If you run a Python script with the -O option then
# python -O habr.py means run with debug == false

# strict type specialization
def getSoup(link: str):
    response = None
    try:
        response = request.urlopen(link)
    except err.URLError as re:
        raise re

    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Method for parsing
# returns a list of tags specified by the parameter 'html_tag'
def parse(soup, html_tag, class_name = None):
    tags = []
    attrs = {}
    if class_name is not None:
        attrs = {'class': class_name}
        
    for post_title in soup.findAll(html_tag, attrs): # tag='article', class_name = 'post post_preview'
        if __debug__: 
            print(post_title)
        tags.append(post_title)
    return tags

# usage example:
soup = getSoup("https://habr.com/en/flows/develop/")
listOfTags = parse(soup, 'article', 'post post_preview')
