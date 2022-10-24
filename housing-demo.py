import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')
st.title('California Housing Data(1990)by Cui Jiayu')
df = pd.read_csv('housing.csv') 
price_filter = st.slider('Median House Price:', 0, 500001, 200000)
df = df[df.median_house_value <= price_filter]

# create a multi select
price_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults



# # filter by capital
# df = df[df.capital.isin(capital_filter)]

#widget to select
level = st.sidebar.radio('Choose income level', ('Low','Medium','High'))
if level == 'Low':
    df = df[df.median_income <= 2.5]
elif level == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income >= 4.5]

st.map(df)

st.subheader('Histogram of the Median House Value')
fig,ax = plt.subplots(figsize=(12,8))
median_house_value = df.median_house_value
df.median_house_value.hist(bins=30)

st.pyplot(fig)