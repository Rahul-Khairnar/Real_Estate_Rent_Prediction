# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:59:58 2020

@author: RAHUL KHAIRNAR
"""
import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_rent(locality,area,bathroom_num,bedroom_num):
    try:
        loc_index = __data_columns.index(locality.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = bathroom_num
    x[2] = bedroom_num
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("Loading the saved artifacts....")
    global __data_columns
    global __locations
    
    with open("E:\PROJECTS\REAL_ESTATE_RENT_PREDICTION\server\Artifacts\columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        
    global __model
    if __model is None:    
        with open("E:\PROJECTS\REAL_ESTATE_RENT_PREDICTION\server\Artifacts\Mumbai_house_rent_prediction_model.pickle","rb") as f:
            __model = pickle.load(f)

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

        
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_rent("Lokhandwala Twp",1090,2,2))