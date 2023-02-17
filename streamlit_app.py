import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('Smoked Salmon and Scrambled Eggs 🐔')
streamlit.text('Overnight Oats 🥣')
streamlit.text('Smashed Avocado on Toast 🥑🍞')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display results
streamlit.dataframe(my_fruit_list)
