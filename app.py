import streamlit as st

def main():
    st.set_page_config(page_title="Chat con varios PDFs", page_icon="books:")

    st.header("Chat con varios PDFs :books:")
    st.chat_input("Pregunta sobre tus documetos")

    with st.sidebar:
        st.subheader("Tus documentos")
        st.file_uploader("Sube tus pdfs aqui y click en 'Procesar'")
        st.button("Process")
    
    
    



if __name__ == '__main__':
    main()