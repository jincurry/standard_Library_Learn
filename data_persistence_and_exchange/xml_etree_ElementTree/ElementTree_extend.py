from xml.etree.ElementTree import Element

from ElementTree_pretty import prettify

top = Element('top')

child = [
    Element('child', num=str(i)) for i in range(3)
]

top.extend(child)
print(prettify(top))
