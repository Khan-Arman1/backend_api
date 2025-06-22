
import json # convert data to json
from utility.NewSyntax import *

# convert to oops
class Finish_Response:
   
  def __init__(self,prompt):
      self.prompt = prompt
    
  def finish_response(self):
      """Convert the search_output result into a json format(dictionary).
          We can access the data using the keys,
          This will give a behaviour to object
      """
      try:
        NewSyntax_object1 = Search_Output(self.prompt) # NS_obj.search_output() will return string llm response
        returnedresponse = NewSyntax_object1.search_output_solid() # constructor

        data = json.loads(returnedresponse) # loads to the json formate to change the datatype
        if type(data) == str(): # if still the type if string then again pass the prompt to the finish_response class
          prompt2 = self.prompt
          NewSyntax_object2 = Search_Output(self.prompt) # NS_obj.search_output() will return string llm response
          returnedresponse = NewSyntax_object2.search_output_solid() # constructor

      
      except Exception as E: # if try block raise an error when loading to the json
        NewSyntax_object3 = Search_Output(self.prompt)
        returnedresponse = NewSyntax_object3.search_output_stream()
        # x = str(E)
        # x = "Sorry, can you please enter your query again😉!"
        data = returnedresponse
        """Better option is to pass the prompt again the llm model , after that either it returns stream output or a complete output"""

      return data
      

########################

