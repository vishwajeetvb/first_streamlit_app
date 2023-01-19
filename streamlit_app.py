import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Parents New Healthy Diner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Added a picker for fruits picking
fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Added a dataframe for fruits table
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
  

#added a input box
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a group to get information.")
  else:
      back_from_function=get+fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_fucntion)      
      
except URLError as e:
    streamlit.error()


streamlit.header("The fruit load list contains:")
#Snowflake related fucntion
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
    
#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

    
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values (' " +new_fruit+ " ') ")
        return "Thanks for adding " + new_fruit
        

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)
    





