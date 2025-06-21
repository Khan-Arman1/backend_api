# print("NewSyntax start executing...")

# import necessary libraries
from utility.config import client # set configurations
from utility.documents import *
from google.genai import types # for understanding the document by model
from utility.instructions import *
import re # regular expression
#---

class search_output:
  
  def __init__(self,prompt):
    self.prompt = prompt


  # def search_output(prompt):
  def search_output(self):

    print(f"Prompt reached successfull : {self.prompt}")
    """ this function interacts with the google model, sends query and return resposne, Here i have create 3 models for different works
    """
    expression = re.findall("reason of providing data from bns according to query|reason of providing data from bnss according to query|reason of providing data from ipc according to query|reason of providing data from evidence law according|reason of providing data from motor vehicle act according to query|reason of providing data from human rights according|reason of providing data from protection of women from domestic violence according to query|reason of providing|why you give|how can say that",(self.prompt).lower())
    if expression:
      """ if a user asks the reason of providing some data by copying the returned response, the regular expression checks whether the prompt satisfy the condition, if yes then this will executed
      """
      response=client.models.generate_content(
      model='gemini-2.0-flash-001',
      contents=[BNS(),BNSS(),EVIDENCE(),HUMAN_RIGHTS(),VEHICLE(),WOMEN_PROTECTION(),self.prompt],
      config=types.GenerateContentConfig(
          system_instruction=INSTRUCTION_1,
          temperature=0.8,
          response_mime_type= 'application/json',
      ),
      )
      # print("Reguler Expression")
      # print(response.text)
      return response.text



      ##################################################
    elif len(self.prompt.split()) < 11:
      """ this checks the len if the length is < 11 then this will execute. 
      this model answers uses normal querys.
      ex- what are you, your name, what can you do for me, user asks for some specific section or act or law, etc."""
      response=client.models.generate_content(
      model='gemini-2.0-flash-001',
      contents=[BNS(),BNSS(),EVIDENCE(),HUMAN_RIGHTS(),VEHICLE(),WOMEN_PROTECTION(),self.prompt],
      config=types.GenerateContentConfig(
          system_instruction=INSTRUCTION_2,
          temperature=0.8,
          response_mime_type= 'application/json',
      ),
      )
      # print("Simple Non Reguler Expression")
      # print(response.text)
      return response.text





      ##################################################
    elif len(self.prompt.split()) < 26 and len(self.prompt.split()) > 10:
      """ this checks the len if the length is <= 25 then this will execute. 
      this model answers uses normal querys.
      ex- what are you, your name, what can you do for me, user asks for some specific section or act or law, etc."""
      response=client.models.generate_content(
      model='gemini-2.0-flash-001',
      contents=[BNS(),BNSS(),EVIDENCE(),HUMAN_RIGHTS(),VEHICLE(),WOMEN_PROTECTION(),self.prompt],
      config=types.GenerateContentConfig(
          system_instruction=INSTRUCTION_3,

          temperature=0.8,
          response_mime_type= 'application/json',
      ),
      )
      # print("Simple Non Reguler Expression")
      # print(response.text)
      return response.text

      ##################################################
    else:
      """This is the last model that performs the actual working. 
      Returned the response of a case user asks"""
      response=client.models.generate_content(
      model='gemini-2.0-flash-001',
      contents=[BNS(),BNSS(),EVIDENCE(),HUMAN_RIGHTS(),VEHICLE(),WOMEN_PROTECTION(),self.prompt],
      config=types.GenerateContentConfig(
          system_instruction= INSTRUCTION_4,
          temperature=0.8,
          response_mime_type= 'application/json',

      ),
      )

      # print("None Reguler Expression")
      # print(response.text)
      return response.text


# print("NewSyntax end executing...")
