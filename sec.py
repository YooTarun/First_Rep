import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
figs = st.container()

with header:
    st.title('Streamlit')

with dataset:
    st.subheader('Dataset')
    data = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    st.write(data.head(2))

    st.subheader('Plots for count of car brands in the city')
    city = st.selectbox('Select a city to plot',options=data['City'].unique())
    filtered_data = data[data['City']==city]
    st.write(filtered_data.head(2))
    st.subheader(f'Top 10 car brands in {city}')
    brand_count = pd.DataFrame(filtered_data['Make'].value_counts().head(10))
    st.bar_chart(brand_count)

with figs:
    year = st.selectbox('Select year',options=data['Model Year'].unique())
    filtered_year = data[data['Model Year']==year]
    st.subheader(f'Count of cars manufactured in {year}')
    cars_prod_count = pd.DataFrame(filtered_year['Make'].value_counts().head(10))
    st.bar_chart(cars_prod_count)

with figs:
    top_electric_range = data.groupby('Make')['Electric Range'].max().reset_index()
    brand = st.selectbox('Select a brand',options=data['Make'].unique())
    selected_value = top_electric_range[top_electric_range['Make'] == brand]['Electric Range'].values[0]
    st.write(f'Maximum range for {brand} is {selected_value}')