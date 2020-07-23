# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:20:21 2020

@author: RAHUL KHAIRNAR
"""
from flask import Flask, request, jsonify
import util

app = Flask(__name__)
## DEFINING THE HTTP END POINT. THE BELOW IS THE CODE FOR ROUTINE
@app.route('/hello')
## IMPORTING THE JSON FILES WITH ALL THE LOCATION
def get_location_names():
    response = jsonify({
        'location':util.get_location_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    return 'Hi!'

if __name__ == '__main__':
    print("Starting the FLask Server for Property Rent Production....")
    app.run()
