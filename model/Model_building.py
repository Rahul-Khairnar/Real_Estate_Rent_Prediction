import pandas as pd
import numpy as np
import pickle
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("Properties_cleaned.csv")
df_dummy = pd.get_dummies(df)

df_final = df_dummy.drop("locality_Others",axis = 1)

df_without_dependent = df_final.drop("price",axis = 1)
df_dependent = df_final["price"]


X_train,X_test,y_train,y_test = train_test_split(df_without_dependent,df_dependent,test_size=0.3,random_state=10)   

#LINEAR REGRESSION
lr_model = RandomForestRegressor(n_estimators = 200,criterion="mse")
lr_model.fit(X_train,y_train)
lr_model.score(X_test,y_test)

linear_model = LinearRegression(normalize = False)
linear_model.fit(X_train,y_train)
linear_model.score(X_test,y_test)

cv = ShuffleSplit(n_splits = 5,test_size = 0.2, random_state = 0)
cross_val_score(lr_model,df_without_dependent,df_dependent,cv=cv)


def best_model_grid_search(X,y):
    algos = {'linear_regression':
             {'model':LinearRegression(),'params':{'normalize':[True,False]}},'lasso':{'model':Lasso(),
            'params':{'alpha':[1,2],
            'selection':['random','cyclic']}},
            'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{'criterion':['mse','friedman_mse'],
            'splitter':['best','random']}
            }
    }
    scores = []
    cv = ShuffleSplit(n_splits=5,test_size=0.3,random_state=300)
    for algo_name,config in algos.items():
        gs = GridSearchCV(config['model'],config['params'],cv=cv,return_train_score=False)
        gs.fit(X,y)
        scores.append({'model':algo_name,'best_score':gs.best_score_,'best_params':gs.best_params_
        })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])

best_model_grid_search(df_without_dependent,df_dependent)

def predict_price(location,sqft,bathrooms,bedrooms):
    loc_index = np.where(df_without_dependent.columns==location)[0]
    print(loc_index)
    
    x = np.zeros(len(df_without_dependent.columns))
    x[0] = sqft
    x[1] = bathrooms
    x[2] = bedrooms
    if loc_index >= 0:
        x[loc_index] = 1
    return lr_model.predict([x])[0]

predict_price("Film City Road",950,2,2)

with open("Mumbai_house_rent_prediction_model.pickle","wb") as f:
    pickle.dump(lr_model,f)
    
df_without_dependent.columns

columns = {
    'data_columns':[col.lower() for col in df_without_dependent.columns]
    }
with open("columns.json","w") as f:
    f.write(json.dumps(columns))


                