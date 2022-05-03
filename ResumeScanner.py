import streamlit as st
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfFileReader 

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Match your Resume with Job description")



uploaded_Resume = st.sidebar.file_uploader("Upload your resume", ["docx", "pdf"])

def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()

    return all_page_text

with col1:
    st.markdown("##")    
    if uploaded_Resume is not None:
        if uploaded_Resume.type == "application/pdf":
            uploaded_Resume = read_pdf(uploaded_Resume)
            st.write(uploaded_Resume)

        else:
            uploaded_Resume = docx2txt.process(uploaded_Resume)
            st.write(uploaded_Resume)

uploaded_Job_description = st.sidebar.file_uploader("Upload job description", ["docx"])

with col2:
    #st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown('##')
    if uploaded_Job_description is not None:
        uploaded_Job_description = docx2txt.process(uploaded_Job_description)
        st.write(uploaded_Job_description)


text = [uploaded_Resume, uploaded_Job_description]


cv = CountVectorizer()
try:
    count_matrix = cv.fit_transform(text)
    #st.write(cosine_similarity(count_matrix))
    match_Percentage = cosine_similarity(count_matrix)[0][1] * 100
    match_Percentage = round(match_Percentage, 0)
except:
    st.stop()

st.sidebar.write("Your resume matches about " + str(match_Percentage)+ "% of the job description")


