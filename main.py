from pdf2docx import Converter
import streamlit as st
import os
import tempfile

st.title("pdf to docx")


uploaded_file = st.file_uploader("File upload")
if uploaded_file:
    with st.spinner('Cargando datos ...'):
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, uploaded_file.name)
        docx_path = path.replace('.pdf','.docx')
        docx_filename = uploaded_file.name.replace('.pdf','.docx')
        if uploaded_file.type == 'application/pdf':
            with open(path, "wb") as f:
                f.write(uploaded_file.getvalue())
        cv = Converter(path)
        cv.convert(docx_path)
        cv.close()


        with open(docx_path, 'rb') as f:
            st.download_button('Download docx', f, file_name=docx_filename)






