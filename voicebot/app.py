import requests
import speech_recognition as sr     # import the library

 
bot_message = ""
message=""

r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": "welcome"})

print("Bot says,  ",end=' ')  ## MH 01 HL 1232
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

while bot_message != "bye" or bot_message!='thanks': 

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Listening :")

        r.energy_threshold = 50
        r.dynamic_energy_threshold = False      # noise reduction

        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio, language="en-IN")  # use recognizer to convert our audio into text part.
            print("You said : {}".format(message))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message)==0:
        continue
    
    if message=='bye' or message=='goodbye':
        print('Have a nice day ahead.')   # end program when user says bye
        break

    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")
