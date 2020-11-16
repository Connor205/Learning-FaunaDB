import re
import json

with open("khoury_people.txt", "r") as f:
    people_text = f.read()

links = list(set(re.findall('(?<=ata-glasslinktarget=").*(?=">)',
                            people_text)))
with open("khoury_links.txt", "w+") as w:
    json.dump(links, w)
