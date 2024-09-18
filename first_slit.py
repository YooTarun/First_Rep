import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()
plot_cols = st.container()

with header:
    st.title('streamlit proj')

with dataset:
    st.title('this is a dataset')
    
    data=pd.read_csv('Electric_Vehicle_Population_Data.csv')
    st.write(data.head())

    dist_plot = pd.DataFrame(data['Make'].value_counts())
    st.bar_chart(dist_plot)

with plot_cols:
    plot_cols = st.columns(1)
    select_col = plot_cols[0]
    cols = select_col.selectbox('wanted_cols',options=data.columns,index=0)

with model_training:
    st.header('Model')

with model_training:
    selection_col,display_col =st.columns(2)

    max_depth= selection_col.slider('Max_depth model',min_value = 10.0,max_value=20.0,value=15.0,step=0.1)

    n_estimators = selection_col.selectbox('Number of estimators',options=[10,20,30,40],index=0)

    input_features = selection_col.selectbox('Features_wanted',options=data.columns,index=0)
