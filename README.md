## Real Estate Rent Prediction - Project Overview

* Created a web application that takes some inputs like Locality, Number of bedrooms, Number of bathrooms, and the Area in square feet. 
* The application is designed using HTML. CSS in the front end and Javascript, JQuery and Python Flask in the backend.
* The model uses a RandomForestsRegresson() to predict the rent.

## Resources used and referred to

* Languages used -
    * Python
    * Javascript
    * JQuery
    * HTML
    * CSS

* Tools used - Postman, Jupyter notebook, Spyder IDE, Sublime Text 3
* Modules used - Pickle, Jsonify, Matplotlib, Seaborn, Pandas, Numpy, Flask, Sklearn
* Web development framework - Flask

## About the dataset - Property data

* The dataset originally contained all the details of properties for eg: Latitudes, Longitudes, Link, Bathroom count, Bedroom count etc.
* Columns import for model building are separated into a new dataframe. Columns include :-
    * Area in square foot
    * Number of bedrooms
    * Number of bathrooms
    * Locality
    * Rent

* The dataset has about 34000 rows consisting of properties from various localities from across the various suburbs of Mumbai.
* The rents start from as low as 7k and as high as 5 Lacs.
* Various properties included flats from a 1bhk flat to 5bhk flat.

## Data Cleaning and Exploration

* The dataset contained outliers. For example:-
    * Prize of 2bhk flat with same area and same locality greater than a 3bhk flat.
    * 2bhk flat with area less than 400 square feet.
    * Rent of flats greater than 2 Lacs which acted as an outlier.

* Apart from outliers, the dataset contained some localities with just one property. Thus to reduce the number of features after conversion of the dataframe to dummies,
the localities with one property were converted to Other.

## Exploratory Data Analysis

* Top localities with most number of properties.
* To check what is the total number of bathrooms and bedrooms in the properties available.
* Heat map to check for correlation between Area, Number of bedrooms, Number of bathrooms and prices.

## Model Building

* Dummy data is divided into a ratio of 70%-30% into train and test sets respectively. 
* Different models tried:-
    * Decision Tree Regressor
    * Random Forest Regresson
    * Linear Regression
    * Lasso Regression

* I used GridSearchCV to check which algorithm performs the best, and at what parameters it performs the best.
* From the results obtained, Random Forest performed the best followed by Linear Regression. Decision Tree performed the worst with accuracy of just 40%.
* Random forests performed best at n_estimators = 200, criterion = "mse".

## Flask Server

* The model is exported to a pickle file.
* The columns necessary for the web application are saved inside a json file.
* Flask module is used to create a flask server.
* Two routines are created:-
    * Routine 1 for getting all the locations
    * Routine 2 for getting the predicted rent.

* Two python files are created:-
    * Server.py - Contains both the routines.
    * Util.py - Contains the functions to import the models from the pickle file and columns from the json file.

* On running the server and the predict_house_rent() routine with parameters, the predicted rent is displayed as an output.

## Productionization - Web Application

* Mumbai Property Rent Predictor is developed using HTML, CSS, Javascript and JQuery.
* The website UI is very simply and easy to use.


