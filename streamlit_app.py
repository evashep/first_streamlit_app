import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('Smoked Salmon and Scrambled Eggs 🐔')
streamlit.text('Overnight Oats 🥣')
streamlit.text('Smashed Avocado on Toast 🥑🍞')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# setting fruit names as the index 
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display results
streamlit.dataframe(fruits_to_show)



# fruityvice api response 
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
streamlit.text(fruityvice_response)



# normalise json version
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display normalised version
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


# allow user to add fruit to the list 
add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
