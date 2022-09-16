import json,time
from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
import requests
import speech_recognition as sr 


app=Flask(__name__)
output=[]

@app.route('/')
def home_page():
    return render_template("IY_Home_page.html",result=output)


@app.route('/result',methods=["POST","GET"])
def Result():
    if request.method=="POST":
        print(list(request.form.values()))
        result=list(request.form.values())[0]
        if result.lower()=="restart":
            output.clear()
        else:
            
                r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                print("Bot says, ")
                for i in r.json():
                    bot_message = i['text']
                    print(f"{bot_message}")
                
                while bot_message != "bye" or bot_message!='thanks': 

                    r = sr.Recognizer()  # initialize recognizer
                    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
                        print("Listening :")
                        r.energy_threshold = 50
                        r.dynamic_energy_threshold = False       # noise reduction
                        audio = r.listen(source)  # listen to the source
                        try:
                            message = r.recognize_google(audio, language="en-IN")  # use recognizer to convert our audio into text part.
                            result = message

                        except:
                            result = "Sorry could not recognize your voice"  # In case of voice not recognized  clearly
                    if len(message)==0:
                        continue
                    
                    print(result)

                    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                    print("Bot says, ",end=' ')
                    for i in r.json():
                        bot_message = i['text']
                        print(f"{bot_message}")

                    output.extend([("Client",result),("Bot",bot_message)])
        return render_template("IY_Home_page.html",result=output)

if __name__=="__main__":
    app.run(debug=True)
