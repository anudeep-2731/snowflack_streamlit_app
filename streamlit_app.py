import streamlit
import pandas as pd
import snowflake.connecter

streamlit.title("Anudeep Basva")

streamlit.header("Breakfast menu")

streamlit.text("🥣dosa")

myfruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

myfruit_list=myfruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruites:",list(myfruit_list.index),['Avocado'])

myfruits_show=myfruit_list.loc[fruits_selected]

streamlit.dataframe(myfruits_show)
