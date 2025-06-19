from utility import convertor_ as ucjson
# from utility.NewSyntax import search_output
from markupsafe import escape
from flask import *
from datetime import date
from flask_cors import CORS
from random import randint

# initiallize the flask app
app=Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}) # allows only specific frontend domain


app.secret_key = "adfjskasjflkjasflksfja13"

# response = { ' ' : "Hello, My name is Legola, A AI Legal Advisor."}
response = "Hello, My name is Legola, A AI Legal Advisor."
input_case=""
greeting = ["hy","hello","hi","hii","hyy","hye","hee","he"]
# credit = 10

# index page (main page)
@app.route('/api/requestdata',methods=['GET','POST'])
# @app.route('/',methods=['GET','POST'])
def index_page():
            global response,credit
        # while credit > 0:
            try:
                if True:
                    # print("Credits remain -",credit)
                    # credit -= 1 
                    # if credit >0:
                        
                        if request.method == "POST":
                            input_case=request.form[escape('cases')].lower()
                            print("Your entered query-- ",input_case)
                            # calling the resposne function
                            if input_case.isnumeric():
                                # response = {' ': "Sorry, I can't process numbers only."}
                                response = "Sorry, I can't process numbers only."
                                return jsonify(response)
                                # return jsonify({" ":response})

                            if input_case in greeting:
                                # response = {' ': "Hy"}
                                localgreeting = ["hello","hi","hii","hy"]
                                response = greeting[randint(0,len(localgreeting)-1)].capitalize()
                                return jsonify(response)
                                # return jsonify({" ":response})

                            if input_case in greeting:
                                # response = {' ': "Hy"}
                                localgreeting = ["i love you","iloveyou","ilove you","i loveyou", "you love me", "youlove me", "you loveme", "youloveme"]
                                response = greeting[randint(0,len(localgreeting)-1)].capitalize()
                                return jsonify(response)
                                # return jsonify({" ":response})

                            elif input_case.isspace():
                                # response = {' ': "I can't process whitespaces."}
                                response = "I can't process whitespaces."
                                return jsonify(response)
                                # return jsonify({" ":response})

                            elif (input_case == "what is your name") or (input_case == "what is your name?") or (input_case == "what is your name."):
                                # response = {' ': "I can't process this. Enter a valid query."}
                                localname = ["My name is Yudhir.","I'm Yudhir."]
                                response = localname[randint(0,len(localname)-1)]
                                return jsonify(response)
                                # return jsonify({" ":response})

                            elif (input_case == "what are you") or (input_case == "what are you?") or (input_case == "what are you."):
                                # response = {' ': "I can't process this. Enter a valid query."}
                                localintro = ["I am Yudhir, a professional legal advisor. To provide you with specific legal advice, please provide me with the details of the legal matter, including the relevant facts, documents, and the specific questions you have. I will then analyze the information and offer guidance based on my understanding of the law.","Provides legal advice based on the provided legal data."]
                                response = localintro[randint(0,len(localintro)-1)]
                                return jsonify(response)
                                # return jsonify({" ":response})
                                
                            elif (input_case == "how can you help me") or (input_case == "how can you help me?") or (input_case == "how can you help me.") or (input_case == "how can you help me!") or (input_case == "help") or (input_case == "help!") or (input_case == "can you help me") or (input_case == "can you help me.") or (input_case == "can you help me?") or (input_case == "can you help me!") or (input_case == "help me") or (input_case == "help me.") or (input_case == "help me!") or (input_case == "help me?") or (input_case == "what can you do") or (input_case == "what can you do.") or (input_case == "what can you do?") or (input_case == "what can you do!") or (input_case == "what can you do for me") or (input_case == "what can you do for me.") or (input_case == "what can you do for me?") or (input_case == "what can you do for me!"):
                                # response = {' ': "I can't process this. Enter a valid query."}
                                localhelp = ["I can provide legal information, explain legal concepts, and offer insights into various laws based on the data I have. I can also help you understand the implications of legal provisions and offer guidance, but remember, I am not a substitute for a qualified legal professional. I am here to assist you to the best of my ability with the knowledge I possess.","I can provide legal information, explain laws, and offer guidance based on the data I have. What specifically do you need help with?","I am Yudhir, your professional legal advisor. Please provide your query, and I will do my best to assist you with legal information and advice. Note that this is not a substitute for consulting a licensed attorney."]
                                response = localhelp[randint(0,len(localhelp)-1)]
                                return jsonify(response)
                                # return jsonify({" ":response})
                                
                            else: 
                                try:
                                    response=ucjson.finish_response(input_case)
                                    # print(credit)
                                    # credit -= 1 
                                    
                                    if type(response) is type({'a':'1',1:'asdf'}):
                                        print(type(response))
                                        # print(response)
                                        return jsonify(response)
                                        # return jsonify({" ":response})
                                    elif type(response) is type(list('aran')):
                                        # print(response)
                                        print(type(response))
                                        return jsonify(response)
                                        # return jsonify({" ":response})
                                except:
                                    response=ucjson.finish_response(input_case)
                                    # print(credit)
                                    # credit -= 1 
                                    # response=search_output(input_case) # from NewSyntax

                                    if type(response) is type({'a':'1',1:'asdf'}):
                                        print(type(response))
                                        # print(response)
                                        return jsonify(response)
                                        # return jsonify({" ":response})
                                    elif type(response) is type(list('aran')):
                                        # print(response)
                                        print(type(response))
                                        return jsonify(response)
                                        # return jsonify({" ":response})
                        print("Credits remain - ",credit)
                    

                    # elif credit == 0:
                    #     response = "You are out of credits. Create an account for more actions."
                    #     print("Credits remain - ",credit)
                    #     return jsonify(response)
                    #     # return jsonify({"error":response})
                    # elif credit < 0:
                    #     response = "You are out of credits. Create an account for more actions."
                    #     print("Credits remain - ",credit)
                    #     return jsonify(response)
                    #     # return jsonify({"error":response})

            except Exception as e:
                 response = "Sorry, can you please enter your query again😉"
                 return jsonify(response)
                #  return jsonify({"error":response})
            
            
# Server par Flask port dynamically handle karna
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

