import glob
import sys
from threading import Thread
from django.shortcuts import redirect, render
from numpy import delete
from sklearn.metrics import accuracy_score

from app import atot
from . import getmodel,reading,clear,predict

flag=""
emo={'calm':"128522",'neutral':"128578",'sad':"128557",'happy':"128514",'angry':"128545",'fear':"128552",'disgust':"128556",'surprise':"128558"}
global t
model,accuracy=model,accuracy=getmodel.l(r"C:\Users\Admin\OneDrive\Desktop\SPDY\SIT\MAJOR\Pro\VAI\media\model")
t=None

    
def index(request):
    print("  Home Page  ".center(100,"."))   
    return render(request,'index.html',{'design':flag})

def start(request):
    print("  Listening Voice ".center(100,"."))   
    clear.clear()
    global t
    if(not t==None):
        if(isinstance(t, (Thread,reading.VoiceT))):
            if(t.is_live()):
                t.start()
    elif(t==None):
        t=reading.VoiceT()
        t.start()
    print()
    print("".center(100,"-"))
    print("  Reading and Fragmenting Chunks Done  ".center(100," "))
    print("".center(100,"-"))
    return render(request,'start.html',{'design':flag})

def end(request):
    global t
    res=predict.predict(model)
    km=max(zip(res.values(), res.keys()))[1]
    # textfromspeak=atot.converttext()
    textfromspeak=''
    try:
        t.stopread()
    except:
        t=None
    t=None
    acc="{0}".format(round(accuracy,2))

    return render(request,'end.html',{'design':flag,"emo":emo,"km":km,"result":res,"emoji":str(emo[km]),"accuracy":acc,"text":textfromspeak,"nchunks":sum(res.values())//3})


