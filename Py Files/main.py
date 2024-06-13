import streamlit as st
import helper_langchain

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "Sri Lankan"))

def generate_restaurant_name_items(cuisine):
    return {
        'restaurant_name': 'Curry Delight',
        'menu_items' : 'Samosa, paneer tikka'
    }

if cuisine:
    response = helper_langchain.generate_restaurant_name_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("",item)