import os
import pyttsx3 as pt
pt.speak("Use the following key words to start the application")
print("Keywords : run,  open,  play,  execute,  browse,  start")
print("For example: start chrome")
while True:
    pt.speak("Enter the application you would like to work with?")
    app = input("Enter the application you would like to work with? ")
    inp = app.lower()
    if ("run" in inp) or ("open" in inp) or ("play" in inp) or ("execute" in inp) or ("browse" in inp) or ("start" in inp):      
        if ("chrome" in inp):
            pt.speak("opening chrome")
            os.system("chrome")
        elif "firefox" in inp:
            pt.speak("opening firefox")
            os.system("firefox")
        elif "notepad" in inp:
            pt.speak("opening notepad")
            os.system("notepad")
        elif "wmplayer" in inp:
            pt.speak("opening Windows Media Player")
            os.system("wmplayer")
        elif "vlc" in inp:
            pt.speak("opening V L C Media Player")
            os.system("vlc")      
    else:
        pt.speak("Invalid input")
        print("Invalid input")
    pt.speak("Do you want me to open any other application?")
    print("Do you want me to open any other application?")
    pt.speak("Type yes or no to proceed")
    print("yes or no")
    int2=input()
    ans=int2.lower()
    if (ans == "yes") or (ans=="s") or (ans=="y"):
        pt.speak("Your answer is yes")
        continue
    elif (ans=="no") or (ans=="n") or (ans==" "):
        pt.speak("Your answer is no")
        break
pt.speak("Thank you user!")
pt.speak("At your service!")
exit()

