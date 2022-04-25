import speech_recognition as sr
from os import listdir
from os.path import isfile, join

def converttext():
    fh = open("media/text/recognized.txt", "w+")
        # create a speech recognition object
    r = sr.Recognizer()

    i=([f for f in listdir('./media/chunks/') if isfile(join('./media/chunks/', f))])

    filer = r"media/chunks/"
        # recognize the chunk
    for j in i:
        file=filer+j
        with sr.AudioFile(file) as source:
                # remove this if it is not working
                # correctly.
            r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)
  
        try:
                # try converting it to text
            rec = r.recognize_google(audio_listened)
                # write the output to the file.
            fh.write(rec+". ")
        except :
            print("Can't rec this chunk...")
    fh.close()
    fh=open("media/text/recognized.txt", "r+")
    text=fh.read()
    return text
