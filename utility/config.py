
from google import genai # for model use
import os # for import the API key from the file
from dotenv import load_dotenv # load the env file

# loading the fucntion
load_dotenv()

# create a api key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) # access the api key for the google model interaction
# #---

