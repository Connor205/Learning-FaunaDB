from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from tqdm import tqdm
import pprint
import json

f = open(".faunarc", "r")
testDatabaseKey = f.readline()[10:]
f.close()
# print(testDatabaseKey)

client = FaunaClient(testDatabaseKey)

# indexes = client.query(q.paginate(q.indexes()))
# pprint.pprint(indexes)

with open("classes.txt", "r") as f:
    classes_dict = json.load(f)

# print(list(classes_dict.keys()))

for c in tqdm(list(classes_dict.keys())[5:]):
    data_dict = {
        "identifier": classes_dict[c]["course_abbrev"],
        "course_num": classes_dict[c]["course_number"],
        "full_identifier": c,
        "department": classes_dict[c]["department"],
        "description": classes_dict[c]["description"],
        "credit_hours": classes_dict[c]["credit_hours"]
    }
    client.query(q.create(q.collection("Class"), {"data": data_dict}))
