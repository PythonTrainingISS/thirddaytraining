import xml.etree.ElementTree as et
from pprint import pprint as pp

etree = et.parse('movies')  # extension of the file is not required
root_tag=etree.getroot()
print(root_tag.iterfind('title'))
pp(dir(root_tag))# will print all the function supported by this data
pp(root_tag.getchildren())
pp(root_tag.findall(''))

movie_tags = etree.getiterator('movie')

for movie_tag in (root_tag[0],root_tag[-1]):
    print(movie_tag.get('title'))

    for info in movie_tag:
        print('\t', info.tag, ':', info.text)
    print()

#
