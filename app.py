from flask import Flask, render_template, request

import os
from dotenv import find_dotenv, load_dotenv

load_dotenv()
from openai import OpenAI
client = OpenAI(
api_key = os.environ["OPENAI_API_KEY"]
)
# print(openai.api_key)
#Set up Flask app
app= Flask (__name__)

@app.route("/")
def home():
     return render_template("index.html")
# client = OpenAI()
#Define chatbot route
@app.route('/chatbot', methods =["POST"])
def chatbot():
        #  pass
        user_input= request.form["message"]
        prompt = f"User: {user_input}\n Chatbot:"
        chat_history = []
     #    response=client.completions.create(model='curie')
        response= client.completions.create(
          #     model="curie",
               model="text-davinci-003",
         temperature=0.4, 
        prompt=prompt,
        max_tokens=100,
        stop= ["\n User: ", "\nChatbot: "]
        )
      
        # bot_response =response['choices'][0]['text']
        bot_response =response.choices[0].text
     #    bot_response = response['choices'][0]['text']
        chat_history.append(f"User: {user_input}\nChatbot{bot_response} ")

        return render_template(
    "chatbot.html",
    user_input =user_input,
    bot_response =bot_response,
)
if __name__ == "__main__":
   port = os.environ.get("PORT", 5000) #Heroku will set the PORT environment variable for web traffic
   app.run(debug=True, host="0.0.0.0", port=port)


