from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import pprint
import json

f = open(".faunarc", "r")
testDatabaseKey = f.readline()[10:]
f.close()
print(testDatabaseKey)

client = FaunaClient(testDatabaseKey)

indexes = client.query(q.paginate(q.indexes()))