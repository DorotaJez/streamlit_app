import streamlit
import pandas


streamlit.title('New Diner')
streamlit.header('Breakfast')
streamlit.text('Blueberry oatmeal')
streamlit.text('Kale smoothie')
streamlit.text('Eggs')
streamlit.text('Avocado toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt").set_index('Fruit')
streamlit.header('Build your own fruit smoothie')
streamlit.multiselect('Pick some fruits', list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
