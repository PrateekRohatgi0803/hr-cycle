import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_attrition_model():
    data = pd.DataFrame({
        'years_at_company': [1,2,3,5,7,10,12,15],
        'performance_score': [2,3,5,6,4,3,2,1],
        'promotion_last_2yrs': [0,0,1,1,0,0,0,0],
        'left_company': [1,1,0,0,0,1,1,1]
    })
    
    X = data[['years_at_company','performance_score','promotion_last_2yrs']]
    y = data['left_company']
    
    model = RandomForestClassifier()
    model.fit(X,y)
    
    return model

def predict_attrition(model, years, performance, promotion):
    prediction = model.predict([[years, performance, promotion]])
    return prediction[0]