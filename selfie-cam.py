import cv2
import os
import pyttsx3
print("Selfie-cam")
pyttsx3.speak("Welcome to selfie-cam")
print("Enter your filename ")
pyttsx3.speak("Enter your filename")
file=input()
filename=file+'.jpg'
print("0 - Internal webcam       1 - External webcam")
pyttsx3.speak("Enter zero, for internal webcam or Enter one, for external webcam")
print("Select your webcam ")
pyttsx3.speak("Select your webcam")
x=input()
pyttsx3.speak("Camera is setting-up")
while True:
        x=int(x)
        if (x==0) or (x==1):
                cap=cv2.VideoCapture(x)
                print("Press c on the window to capture the image")
                pyttsx3.speak("Press c on the window to capture the image")
                while True:
                        _,image=cap.read()
                        image=cv2.resize(image,(413,531))
                        image=cv2.flip(image,1)
                        cv2.imshow("camera is on", image)
                        if cv2.waitKey(1)& 0xff==ord('c'):
                                cv2.imwrite(filename, image)
                                break
                break
        else:
                pyttsx3.speak("Invalid Entry")
                pyttsx3.speak("Try again")
                continue
cap.release()
cv2.destroyAllWindows()
pyttsx3.speak("Photo was successfully taken")
print("Would you like to view the photo?")
pyttsx3.speak("Would you like to view the photo?")
pyttsx3.speak("Type, yes, to view the photo")
view=input()
if (view=="yes") or (view == "s") or (view=="S") or (view=="Yes") or (view=="y"):
        print("Press q to close the image window")

while True:
        if (view=="yes") or (view == "s") or (view=="S") or (view=="Yes") or (view=="y"):
            read=cv2.imread(filename)
            ima=cv2.imshow(" ", read)
            if cv2.waitKey(1) & 0xff==ord('q'):
                   break
        else:
             pyttsx3.speak("You have selected, no, as your option")
             pyttsx3.speak("Thanking for using the service")
             quit()

cv2.destroyAllWindows()
