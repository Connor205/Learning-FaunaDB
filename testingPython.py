from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import pprint

f = open(".faunarc", "r")
key = f.readline()[10:]
f.close()

client = FaunaClient(key)

indexes = client.query(q.paginate(q.indexes()))

allPeopleAllFields = client.query(q.paginate(q.match(
    q.index("all_people"))))["data"]

for person in allPeopleAllFields:
    print(client.query(q.get(person))["data"])
