import csv
import datetime
from xml.etree.ElementTree import Element, Comment, SubElement

from ElementTree_pretty import prettify

generated_on = str(datetime.datetime.now())

root = Element('opml')
root.set('version', '1.0')

root.append(
    Comment('Genetated by ElementTree_csv_to_xml.py for PyMOTW')
)

head = SubElement(root, 'head')
title = SubElement(head, 'title')
title.text = 'My Podcasts'
dc = SubElement(head, 'dataCreated')
dc.text = generated_on
dm = SubElement(head, 'dataModified')
dm.text = generated_on

body = SubElement(root, 'body')

with open('podcasts.csv', 'rt') as f:
    current_group = None
    reader = csv.reader(f)
    for row in reader:
        group_name, podcast_name, xml_url, html_url = row
        if current_group is None or group_name != current_group.text:
            current_group = SubElement(body, 'putline', {'text': group_name})

        podcast = SubElement(
            current_group, 'outline',
            {
                'text': podcast_name,
                'xmlUrl': xml_url,
                'htmlUrl':html_url,
            },
        )
print(prettify(root))
