from importlib.resources import Package
import os
from keras.models import model_from_json
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


def l(path):
    if(os.path.isdir(path)):
        if(os.path.isfile(path+"/features.csv")):
            try: 
                Features=pd.read_csv(path+"/features.csv")
                X = Features.iloc[: ,:-1].values
                Y = Features['labels'].values
                encoder = OneHotEncoder()
                Y = encoder.fit_transform(np.array(Y).reshape(-1,1)).toarray()
                x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0, shuffle=True)
                scaler = StandardScaler()
                x_train = scaler.fit_transform(x_train)
                x_test = scaler.transform(x_test)
                x_train = np.expand_dims(x_train, axis=2)
                x_test = np.expand_dims(x_test, axis=2)
            except Exception:
                print("sorry error loading Data \n\t please check features.csv file is exists in the path\n",path )
            else:

                json_file = open(path+'/model.json', 'r')
                loaded_model_json = json_file.read()
                json_file.close()
                loaded_model = model_from_json(loaded_model_json)
                # load weights into new model
                loaded_model.load_weights(path+"/model.h5")
                print("Loaded model from disk")
                loaded_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
                accuracy=loaded_model.evaluate(x_test,y_test)[1]*100
                print("Accuracy of our model on test data : " ,accuracy , "%")

                return loaded_model,accuracy

class load:
    def run(self):
        path=self.path
        if(os.path.isdir(path)):
            print("dir")
            if(os.path.isfile(path+"/features.csv")):
                print("file")
                try: 
                    Features=pd.read_csv(path+"/features.csv")
                    X = Features.iloc[: ,:-1].values
                    Y = Features['labels'].values
                    encoder = OneHotEncoder()
                    Y = encoder.fit_transform(np.array(Y).reshape(-1,1)).toarray()
                    x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0, shuffle=True)
                    scaler = StandardScaler()
                    x_train = scaler.fit_transform(x_train)
                    x_test = scaler.transform(x_test)
                    x_train = np.expand_dims(x_train, axis=2)
                    x_test = np.expand_dims(x_test, axis=2)
                except Exception:
                    print("sorry error loading Data \n\t please check features.csv file is exists in the path\n",path )
                else:

                    json_file = open(path+'/model.json', 'r')
                    loaded_model_json = json_file.read()
                    json_file.close()
                    loaded_model = model_from_json(loaded_model_json)
                    # load weights into new model
                    loaded_model.load_weights(path+"/model.h5")
                    print("Loaded model from disk")
                    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
                    accuracy=loaded_model.evaluate(x_test,y_test)[1]*100
                    print("Accuracy of our model on test data : " ,accuracy , "%")

                    return loaded_model,accuracy
    def __init__(self,path):
        self.path=path
        self.run()
    


    

