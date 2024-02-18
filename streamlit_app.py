import streamlit
import pandas as pd

streamlit.title("Anudeep Basva")

streamlit.header("Breakfast menu")

streamlit.text("🥣dosa")

myfruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruits_selected=streamlit.multiselect("Pick some fruites:",list(myfruit_list.Fruit),['Avocado'])

myfruits_show=myfruit_list.loc[fruits_selected]

streamlit.dataframe(myfruits_show)
