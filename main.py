import streamlit as st
import requests

# Prepare the API key and API url
api_key = "6uXee4QNK7lzvn5Yx6whoiasyd72MrsgV92j8lKM"
web_url = ("https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")

# Get the request data as dictionary
response1 = requests.get(web_url)
data = response1.json()

# Extract the title, explanation, image url
title= data["title"]
explanation = data["explanation"]
image_url = data["url"]

# Download the image
response2 = requests.get(image_url)
image_filepath = "image.jpg"
with open(image_filepath, "wb") as file:
    file.write(response2.content)


st.title(title)
st.image(image_url)
# below will also work as we are downloading and the showing
# st.image(image_filepath)
st.write(explanation)