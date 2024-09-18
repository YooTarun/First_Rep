import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

data = pd.read_csv('BostonHousing.csv')

dataset = st.container()
plots = st.container()
model = st.container()

with dataset:
    st.subheader("DataSet")
    st.write(data.head())

with plots:
    st.subheader("Avg House Price for Age")
    age = st.selectbox('Select age value',options = sorted(data['age'].unique()))
    filter_value = data[data['age']==age]
    avg_medv= filter_value['medv'].mean()
    st.write(f'Average price for {age} age is {avg_medv}')

with model:
    st.subheader('Model Training')

    max_depth = st.slider('Max depth',min_value =2,max_value=10,step=1)
    n_estimators = st.slider('Estimators',min_value=50,max_value=300,step=20)
    input_features = st.selectbox('Features',options=data.columns)

    rf_model = RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)

    X = data[[input_features]]
    Y = data[['medv']]
    rf_model.fit(X,Y)
    prediction = rf_model.predict(X)

    st.subheader('Mean Absolute Error')
    st.write(mean_absolute_error(Y,prediction))



