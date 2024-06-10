import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.offline as pyo
import matplotlib.pyplot as plt
import seaborn as sns


st.sidebar.markdown("- Data Frame")
st.sidebar.markdown("- Street Filter")
st.sidebar.markdown("- Marital Status vs Street")
st.sidebar.markdown("- Top fifteen (15) most populated streets.")
st.sidebar.markdown("- Spread of age in United Kingdom ")


st.title('Population Census Analytics Application')

def load_data():
    data = pd.read_csv('cleaned_census_data.csv')  
    return data

df = load_data()
df

st.divider()

# Create a dropdown to select a street name
street_name = st.selectbox('Select a Street', options=df['Street'].unique())

if street_name:
    filtered_data = df[df['Street'] == street_name]
    house_counts = filtered_data.groupby('House Number').size().reset_index(name='Count')
    
    fig = px.line(house_counts, x='House Number', y='Count', title=f'Population in Houses on {street_name}')
    st.plotly_chart(fig)

if street_name:
    marital_status_counts = filtered_data['Marital Status'].value_counts().reset_index()
    marital_status_counts.columns = ['Marital Status', 'Count']
    
    fig = px.bar(marital_status_counts, x='Marital Status', y='Count', title=f'Marital Status Distribution on {street_name}')
    st.plotly_chart(fig)



# Count the number of occurrences for each street
street_counts = df['Street'].value_counts().nlargest(15)

# Filter the DataFrame to only include the top 15 streets
top_streets_df = df[df['Street'].isin(street_counts.index)]

# Group by 'Street Name' and 'Gender' and count occurrences
gender_distribution = top_streets_df.groupby(['Street', 'Gender']).size().unstack(fill_value=0)


# Create a bar chart
fig = px.bar(gender_distribution, 
             title="Gender Distribution Across Top 15 Most Populated Streets",
             labels={"value": "Count", "variable": "Gender"},
             barmode='group')

# Update layout if necessary
fig.update_layout(xaxis_title="Street Name",
                  yaxis_title="Number of People",
                  xaxis={'categoryorder':'total descending'})

st.plotly_chart(fig)

fig = px.scatter(df, x='House Number', y='Age', color='Age', title='Age Distribution Across the UK')
st.plotly_chart(fig)



