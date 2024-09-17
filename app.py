 ## extract text from image

from dotenv import load_dotenv

load_dotenv()  ##load all variable from .env file

import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai 

## config api key

genai.configure(api_key=os.getenv("key")) ## getting the env variable


##function to load gemini pro vison model

def get_gemini_response(input,image,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash') ## loading the model
    response=model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # read file in bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type":uploaded_file.type,  #get mime type of the upload image
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("file upload chey ra osaravalli na kodaka")


## initialize our streamlit

st.set_page_config(page_title="image features extraction 🐦")


st.header("Gemini Image Extracter")
input=st.text_input("Prompt ",key="input")
uploaded_file=st.file_uploader("choose an Image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image, caption="uploaded Image." , use_column_width=True)


submit=st.button("Extract the Features")

input_prompt=""" 
your an expert in understanding invoices you will recieves 
images and you will have to answer the questions based on the 
image.

"""
## submit button after clicking

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)

    st.subheader("the response is")
    st.write(response)















