import streamlit
import pandas as pd
import requests
import snowflake.connector

streamlit.title('New Diner')
streamlit.header('Breakfast')
streamlit.text('Blueberry oatmeal')
streamlit.text('Kale smoothie')
streamlit.text('Eggs')
streamlit.text('Avocado toast')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt").set_index('Fruit')
streamlit.header('Build your own fruit smoothie')
fruits_selected = streamlit.multiselect('Pick some fruits', list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


fruit_choice = streamlit.text_input('What fruit would you like to know about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response.json())

fv_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fv_normalized)


