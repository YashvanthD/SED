
from os import listdir
from os.path import isfile, join

def getnum():
    len([f for f in listdir('./media/chunks/') if isfile(join('./media/chunks/', f))])
