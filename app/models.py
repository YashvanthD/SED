from django.db import models

# Create your models here.
# Python3 program to illustrate store
# efficiently using pickle module
# Module translates an in-memory Python object
# into a serialized byte stream—a string of
# bytes that can be written to any file-like object.

import pickle


def loadData():
	# for reading also binary mode is important
	dbfile = open('model', 'rb')	
	db = pickle.load(dbfile)
    
	dbfile.close()


