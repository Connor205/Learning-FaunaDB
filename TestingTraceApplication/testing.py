import requests
import pprint
import os
import time

f = open("key.txt", "r")
key = f.read()
f.close()

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
  classesByNum(course_num: 2500){
    data {
      full_identifier
      department
    }
  }
}
"""
getClassByID = """
query {
    findClassByID(id:281751816260026882) {
            courseNum
            identifier
            _id
    }
}
"""

findSectionByID = """
query {
  findSectionByID(id: 281830531615687170){
    professor {
      first
      last
    }
    rating
    class {
      fullIdentifier
    }
  }
}
"""

findClassByUnique = """
query {
  classesByFullIdentifier(full_identifier: "CS2500"){
    department
    full_identifier
  }
}
"""

findProfsForClass = """
query getProfessors{
  classesByFullIdentifier(full_identifier: "TEST9999"){
    department
    name
    professors{
      data {
        first
        last
      }
    }
  }
  
}"""
start = time.time()
# Execute the query
# run_query(findProfsForClass)
pprint.pprint(run_query(findProfsForClass)['data'])
end = time.time()
print(f"Runtime of the query is {end - start}")
