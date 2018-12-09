from json import    load,dump

from pprint import pprint as pp

content=load(open('colors.json'))
#install beautifulsoup4 for parsing
content['tasks']