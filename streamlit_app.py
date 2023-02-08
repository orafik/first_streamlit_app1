import streamlit

streamlit.title ('My Mom\'s New Healthy Diner')

streamlit.header ('Breakfast Favorites')

streamlit.text ('Omega 3 & Blueberry Oatmeal')

streamlit.text ('Kale, Spinach & Rocket Smoothie')
                
streamlit.text ('Hard-Boiled Free-Range Egg')

streamlit.text ('Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index))

streamlit.dataframe(my_fruit_list)







import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")

streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
