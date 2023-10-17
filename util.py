import json
import pickle
import os
import numpy as np
__location = None  # Change __locations to __location
__data_columns = None
__model = None



script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, 'details', 'columns.json')
json_file_path1 = os.path.join(script_dir, 'details', 'price_prediction.pickle')


def get_price(location,sqft,bhk,bath):
    try:
         ind=__data_columns.index(location.lower())
    except:
        ind=-1

    x1=np.zeros(len(__data_columns))
    x1[0]=sqft
    x1[1]=bhk
    x1[2]=bath
    if ind>=0:
        x1[ind]=1
    
        return round(__model.predict([x1])[0],2)




def get_details():
    print("loading saved artifacts...start")
    global __data_columns
    global __location  # Change __locations to __location

    with open(json_file_path, 'r') as f:  # Correct the file path
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]
    global __model
    with open(json_file_path1, 'rb') as f:  # Correct the file path
        model = pickle.load(f)
        __model = model  # Assign the loaded model to __model

    print("loading is done...")

def get_location_name():
    return __location

def get_data_columns():
    return __data_columns

if __name__ == "__main__":
    get_details()
    print(get_location_name())
    print(get_price('1st Phase JP Nagar',1000, 2, 2))
