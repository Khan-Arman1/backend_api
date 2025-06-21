# print("convertor executing...")

import json # convert data to json
from utility.NewSyntax import *

# convert to oops
class finish_response:
   
  def __init__(self,prompt):
      self.prompt = prompt
    
  def finish_response(self):
      """Convert the search_output result into a json format(dictionary).
      We can access the data using the keys,
      This will give a behaviour to object
      """
      try:
        # print("try in convertor")
        # print(f"IN convertor file prompt : {self.prompt}")
        # prompt1 = self.prompt
        # returnedresponse = NS.search_output(prompt1) # NS_obj.return_rspo_opt() will return string llm response
        NewSyntax_object = search_output(self.prompt) # NS_obj.return_rspo_opt() will return string llm response
        returnedresponse = NewSyntax_object.search_output() 

        # print("before converting",type(returnedresponse)) # check the response datatype returned by llm model
        data = json.loads(returnedresponse) # loads to the json formate to change the datatype
        if type(data) == str(): # if still the type if string then again pass the prompt to the finish_response class
          # print(f"Type is string - {type(data)}\nAgain generating response!")
          prompt2 = self.prompt
          NSobject = search_output(self.prompt)
          response = NSobject.search_output()

        # print("After parsing into json - ",type(data)) # if data loaded to json successfully
      
      except Exception as E: # if try block raise an error when loading to the json
          # print("Passed in except")
          # print("An Error occured while parsing into json(try)")
          # response=search_output(prompt) 
          # print("before parsing into json - ",type(response))
          # data = json.loads(response)
          x = "Sorry, can you please enter your query again😉!"
          # x = str(E)
          data = {"response":x}

      return data
      

########################

# print("convertor end executing...")
