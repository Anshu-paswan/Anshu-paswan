import openai
import sys
import time
import os
import gtts

green='\033[1;32;40m '
purple='\033[1;35;40m'
cyan='\033[1;36;40m'
openai.api_key = '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'
def sp(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10/ 200)
os.system('clear')
sp(purple+"Hello I'm here for You what can i do for you ?")
#print("Select the Mode :")
#print("1. Text mode\n2. Voice mode")
#usermode = input(" Select the mode :")
while True:
    model = "text-davinci-003"
    
    user = input(purple+"\nEnter Here: ")
    print("lenght of question is :",len(user))
    
    sp(cyan+"Please wait ......")
    if "exit" in user:
        break
    elif "clear" in user:
        os.system('clear')
    if len(user)=="0":
        print("Please type anything")
    completion = openai.Completion.create(model ="text-davinci-003",
    prompt = user,
    max_tokens = 1024,
    temperature = 0.5,
    n = 1,
    stop = None)
    response = completion.choices[0].text
    
    
    print(green+response)
   
    a1 = input(cyan+"Do you like to listen above Output? (Yes/yes/y) :")
    if a1 == "y" or "yes" or "Yes":
        sound = gtts.gTTS(response)
        sound.save("Sound.mp3")
        os.system('play Sound.mp3 ')
        os.system('rm -rf Sound.mp3')
    elif a1 == "n" or "no":
       
       os.system('clear')