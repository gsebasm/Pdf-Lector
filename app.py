import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat con varios PDFs", page_icon="books:")

    st.header("Chat con varios PDFs :books:")
    st.chat_input("Pregunta sobre tus documetos")

    with st.sidebar:
        st.subheader("Tus documentos")
        pdf_docs = st.file_uploader(
            "Sube tus pdfs aqui y click en 'Procesar'", accept_multiple_files=True )
        if st.button("Process"):
           with st.spinner("Procesando"):
            #se obtiene el pdf
               raw_text = get_pdf_text(pdf_docs)

            #los textos se separan chunks

            #creando los vectores

    
    
    



if __name__ == '__main__':
    main()