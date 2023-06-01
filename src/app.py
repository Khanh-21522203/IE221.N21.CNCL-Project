import streamlit as st
from streamlit_option_menu import option_menu
from tasks.MaskText import MaskTextApp
from tasks.OCR import OCRApp
from tasks.QA import QuestionAnswering
from tasks.Translate import TranslatorApp
from tasks.ImageProcessing import ImageProcess

with st.sidebar:
    selected = option_menu(
                menu_title="Main Menu",  
                options=["Fill Masked Text", "Optical Character Recognition", "Translation", "Question Answer Task", "Image Processing"],  # required
                icons=["braces", "camera2", "file-earmark-text", "envelope"], 
                menu_icon="cast", 
                default_index=0,  
                orientation="vertical",
            )
if selected == "Fill Masked Text":
    if 'maskapp' not in st.session_state:
        st.session_state.maskapp = MaskTextApp()
    Maskapp = st.session_state.maskapp
    Maskapp.run()

if selected == "Optical Character Recognition":
    if 'orc' not in st.session_state:
        st.session_state.ocr = OCRApp()
    OCRapp = st.session_state.ocr
    OCRapp.run()  

if selected == "Translation":
    if 'translate' not in st.session_state:
        st.session_state.translate = TranslatorApp()
    translateapp = st.session_state.translate
    translateapp.run()

if selected == "Question Answer Task":
    if 'qa' not in st.session_state:
        st.session_state.qa = QuestionAnswering()
    QAapp = st.session_state.qa
    QAapp.run()

if selected == "Image Processing":
    if 'imgpro' not in st.session_state:
        st.session_state.imgpro = ImageProcess()
    ImgApp = st.session_state.imgpro
    ImgApp.run()