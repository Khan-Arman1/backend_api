from utility import convertor_ as ucjson
# from utility.NewSyntax import search_output
from markupsafe import escape
from flask import *
from datetime import date
from flask_cors import CORS
from random import randint
import os # for import the API key from the file
from dotenv import load_dotenv # load the env file
# import logging
# from logging.handlers import RotatingFileHandler

load_dotenv()

# initiallize the flask app
app=Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}) # allows all frontend domain
app.secret_key = os.getenv("secret_key")

# File Logging setup
# Create logs directory if it doesn't exist
# if not os.path.exists('logs'):
#     os.mkdir('logs')

# # Setup log file handler
# file_handler = RotatingFileHandler('logs/server.log', maxBytes=10240, backupCount=5)
# file_handler.setFormatter(logging.Formatter(
#     '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
# ))

# Set logging level
# file_handler.setLevel(logging.INFO)
# app.logger.addHandler(file_handler)

# # Logging to Console
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
# console_handler.setLevel(logging.INFO)
# app.logger.addHandler(console_handler)


# # Optional: Set default log level for the app
# app.logger.setLevel(logging.INFO)
# app.logger.info('App startup')

# 


# index page (main page)
@app.route('/api/requestdata',methods=['GET','POST'])
def index_page():
            try:
                        app.logger.info("Recieved a new request")
                        if request.method == "POST":
                            input_case=request.form[escape('cases')].lower()
                            # app.logger.info(f"Input received: {input_case}")
                            # calling the resposne function
                            # Local responses
                            # check if all the entered values are numeric
                            if input_case.isnumeric():
                                response = "Sorry, I can't process numbers only."
                                # app.logger.info(f"Response returned: {response}")
                                return jsonify(response)
                            
                            # checks is greeting is in the list
                            greeting = ["hy","hello","hi","hii","hyy","hye","hee","he"]
                            if input_case in greeting:
                                localgreeting = ["hello","hi","hii","hy"]
                                response = greeting[randint(0,len(localgreeting)-1)].capitalize()
                                # app.logger.info(f"Response returned: {response}")
                                return jsonify(response)
                            
                            # check is all the entered characters are spaces
                            elif input_case.isspace():
                                response = "I can't process whitespaces."
                                # app.logger.info(f"Response returned: {response}")
                                return jsonify(response)

                            # check for simple prompts
                            elif (input_case == "what is your name") or (input_case == "what is your name?") or (input_case == "what is your name."):
                                localname = ["My name is Yudhir.","I'm Yudhir."]
                                response = localname[randint(0,len(localname)-1)]
                                # app.logger.info(f"Response returned: {response}")
                                return jsonify(response)

                            # check for simple prompts
                            elif (input_case == "what are you") or (input_case == "what are you?") or (input_case == "what are you."):
                                localintro = ["I am Yudhir, a professional legal advisor. To provide you with specific legal advice, please provide me with the details of the legal matter, including the relevant facts, documents, and the specific questions you have. I will then analyze the information and offer guidance based on my understanding of the law.","Provides legal advice based on the provided legal data."]
                                response = localintro[randint(0,len(localintro)-1)]
                                # app.logger.info(f"Response returned: {response}")
                                return jsonify(response)
                                
                            # check for simple prompts
                            elif (input_case == "how can you help me") or (input_case == "how can you help me?") or (input_case == "how can you help me.") or (input_case == "how can you help me!") or (input_case == "help") or (input_case == "help!") or (input_case == "can you help me") or (input_case == "can you help me.") or (input_case == "can you help me?") or (input_case == "can you help me!") or (input_case == "help me") or (input_case == "help me.") or (input_case == "help me!") or (input_case == "help me?") or (input_case == "what can you do") or (input_case == "what can you do.") or (input_case == "what can you do?") or (input_case == "what can you do!") or (input_case == "what can you do for me") or (input_case == "what can you do for me.") or (input_case == "what can you do for me?") or (input_case == "what can you do for me!"):
                                localhelp = ["I can provide legal information, explain legal concepts, and offer insights into various laws based on the data I have. I can also help you understand the implications of legal provisions and offer guidance, but remember, I am not a substitute for a qualified legal professional. I am here to assist you to the best of my ability with the knowledge I possess.","I can provide legal information, explain laws, and offer guidance based on the data I have. What specifically do you need help with?","I am Yudhir, your professional legal advisor. Please provide your query, and I will do my best to assist you with legal information and advice. Note that this is not a substitute for consulting a licensed attorney."]
                                response = localhelp[randint(0,len(localhelp)-1)]
                                # app.logger.info(f"Response returned: {response}")
                                return jsonify(response)
                            
                            # Local response end -- 

                            # Talking to LLM model starts
                                
                            else: 
                                # if an error occured in passing the data
                                try:
                                    convertor_object=ucjson.Finish_Response(input_case) # create object of finish_response class
                                    response = convertor_object.finish_response()

                                    if type(response) is type({'a':'1',1:'asdf'}):
                                        # app.logger.info(f"Response sent : {response}\n\t of type: {type(response)}")
                                        return jsonify(response)
                                    elif type(response) is type(list('aran')):
                                        # app.logger.info(f"Response sent : {response}\n\t of type: {type(response)}")
                                        return jsonify(response)
                                    elif type(response) == type(str("hellow")):
                                        # app.logger.info(f"Response sent : {response}\n\t of type: {type(response)}")
                                        return response
                                except:
                                    convertor_object=ucjson.Finish_Response(input_case) # create object of finish_response class
                                    response = convertor_object.finish_response()

                                    if type(response) is type({'a':'1',1:'asdf'}):
                                        # app.logger.info(f"Response sent : {response}\n\t of type: {type(response)}")
                                        return jsonify(response)
                                    elif type(response) is type(list('aran')):
                                        # app.logger.info(f"Response sent : {response}\n\t of type: {type(response)}")
                                        return jsonify(response)
                                    elif type(response) == type(str("hellow")):
                                        # app.logger.info(f"Response sent : {response}\n\t of type: {type(response)}")
                                        return response
                    

            except Exception as e:
                 # app.logger.info(f"Error Raised in returning response: {str(e)}")
                 response = "Sorry, can you please enter your query again😉"
                 return jsonify(response),500


# Server par Flask port dynamically handle karna

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)



