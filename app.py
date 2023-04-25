# : Import the libraries for Pandas and Streamlit
import streamlit as st
import pandas as pd

#: Create a title for your application using markdown syntax and the
# Streamlit `write` function.
st.write("# Ice Cream  Application")

# : Create an opening sentence for your application using regular text and
# the Streamlit `write` function.
st.write("# Ice Cream allows you to make sharable dessert web applications.")

# : Create a Pandas dataframe
df = pd.DataFrame({'Vanilla': [1, 2], 'Choco': [3, 4], 'Streamlit Mix': [5, 6]})

# Write the Pandas dataframe to the page
st.write(df)

# : Create a text input box using the Streamlit `text_input` function.
# : Save the input as a variable.
text = st.text_input("Enter a message here")
    
# : Utilize the Streamlit `button` function to display the text input
if st.button("Display the Text Message"):
    st.write(text)


# Bonus
library = st.sidebar.selectbox(
    "What is your favorite Ice Cream Flavor?",
    ("Vanilla", "Choco", "Stream lit Mix")
)

if st.sidebar.button("Display selection"):
    st.sidebar.write(library)
