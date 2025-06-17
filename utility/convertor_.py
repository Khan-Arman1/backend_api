print("convertor executing...")

import json # convert data to json
from utility import NewSyntax as NS

def finish_response(prompt):
  """Convert the search_output result into a json format(dictionary).
  We can access the data using the keys"""
  try:
    print("try in convertor")
    response=NS.search_output(prompt)
    print("before converting",type(response))
    data = json.loads(response)
    if type(data) == str():
      print(f"Type is string - {type(data)}\nAgain generating response!")
      response = finish_response(prompt)

    print("After parsing into json - ",type(data))
  
  except:
      print("Passed in except")
      print("An Error occured while parsing into json(try)")
      # response=search_output(prompt)
      # print("before parsing into json - ",type(response))
      # data = json.loads(response)
      x = "Sorry, can you please enter your query again😉."
      data = {"response":x}

  return data

##############################

print("convertor end executing...")