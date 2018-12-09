import xml.etree.ElementTree as et

etree=et.parse('movies')#extension of the file is not required

movie_tags=etree.getiterator('movie')

for movie_tag in movie_tags:
    print(movie_tag.get('title'))

    for info in movie_tag:
        print('\t',info.tag,':',info.text)
    print()

#
