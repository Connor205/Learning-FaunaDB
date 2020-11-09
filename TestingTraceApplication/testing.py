import requests
import pprint
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)
f = open("key.txt", "r")
key = f.read()

headers = {"authorization": key}


def run_query(query):
    # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://graphql.fauna.com/graphql',
                            json={'query': query},
                            headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(
            "Query failed to run by returning code of {}. {}".format(
                request.status_code, query))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
getAllSection = """
query {
  allSections {
    data {
      class {
        courseNum
      }
      professor {
        first
        last
      }
    }
  }
}
"""

getClassByNum = """
query {
  classesByNum(courseNum: 2500) {
    data {
      identifier
      courseNum
      _id
    }
  }
}
"""

getClassByID = """
query {
    findClassByID(id:281751816260026882) {
            courseNum
            identifier
    }
}
"""

result = run_query(getClassByID)['data']  # Execute the query
pprint.pprint(result)