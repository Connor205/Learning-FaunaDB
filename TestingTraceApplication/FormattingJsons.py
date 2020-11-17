import json
import re

with open('classes.txt', "r") as f:
    classes = json.load(f)
f.close()

for key in classes.keys():
    get_number = re.compile("\d{4,}")
    get_abbrev = re.compile("\D*")
    course_number = get_number.findall(key)[0]
    course_abbrev_match = get_abbrev.match(key)
    course_abbrev = course_abbrev_match.group()
    classes[key]["course_number"] = int(course_number)
    classes[key]["course_abbrev"] = course_abbrev
    classes[key]["full_id"] = course_abbrev + course_number

with open("classes.txt", "w") as f:
    json.dump(classes, f, indent=4)
