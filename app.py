# need field to put jd
# upload pdf
# pdf to image -> processing -> google gemini pro
# prompt templates [multiple prompt]

import google.generativeai as genai
import pdf2image
from PIL import Image
import os
import streamlit as st
from dotenv import load_dotenv
import base64
import io

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.0-pro-exp')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # convert pdf to image using poppler path
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(),
            poppler_path=r"C:\Program Files (x86)\poppler-24.08.0\Library\bin"
        )
        first_page = images[0]

        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                'mime_type': "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    
# streamlit app
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description : ", key="input")
uploaded_file = st.file_uploader("Upload Resume In PDF Format", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("Percentage Match")

input_prompt1 = """
You are an experienced HR with technical experience in the field of any one job role from Generative AI, Data science, Full stack web development, Big data Engineer,
Devops, data analyst, data scientist, your task is to review the provided resume against the job description for these profiles.
please share your professional evaluation on whether the candidate's profile aligns with this role.
Highlight the strengths and weakness of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an experienced HR with technical experience in the field of any one job role from Generative AI, Data science, Full stack web development, Big data Engineer,
Devops, data analyst, data scientist, your task is to review the provided resume against the job description for these profiles.
please share your professional evaluation on whether the candidate's profile aligns with this role or not.
Highlight the strengths and weakness of the applicant and give suggestions to improve with respect to specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS(Application tracking system) scanner with a deep experience in the field of any one job role from Generative AI, Data science, Full stack web development, Big data Engineer,
Devops, data analyst, data scientist and deep ats functionality, your task is to evaluate the provided resume against the provided job description give me the percentage match if the resume matches with the job description.
first the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is ")
        st.write(response)
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is ")
        st.write(response)
