# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:20:21 2020

@author: RAHUL KHAIRNAR
"""
from flask import Flask, request, jsonify
import util

app = Flask(__name__)
## DEFINING THE HTTP END POINT. THE BELOW IS THE CODE FOR ROUTINE

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_rent',methods=['GET','POST'])
def predict_home_rent():
    area = float(request.form['area'])
    locality = request.form['locality']
    bathroom_num = int(request.form['bathroom_num'])
    bedroom_num = int(request.form['bedroom_num'])
    
    response = jsonify({
        'estimated_price':util.get_estimated_rent(locality,area,bathroom_num,bedroom_num)})
   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
if __name__ == '__main__':
    print("Starting the FLask Server for Property Rent Production....")
    util.load_saved_artifacts()
    app.run()
