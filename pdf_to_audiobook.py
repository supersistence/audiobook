  
from PyPDF2 import PdfFileReader
import os
from gtts import gTTS
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Research : Audiofy",page_icon="🎶",layout="centered",initial_sidebar_state="auto",)

def pypdf2(py_pdf_file):
	#py_pdf_file = open(py_pdf_file, 'rb') 
	# create PDFFileReader object to read the file
	pdfReader = PdfFileReader(py_pdf_file)
	# obtain no, of pages
	numOfPages = pdfReader.getNumPages()
	# final return text string
	text = "PDF File name : " + str(pdfReader.getDocumentInfo().title)
	# text list to contain all pdf text 
	text_lst = list()
	# itterate over all pages
	for i in range(0, numOfPages):
		# obtain page no.
		pageObj = pdfReader.getPage(i)
		# append page content to list
		text_lst.append('\n' + pageObj.extractText())
	# close the PDF file object
	py_pdf_file.close()
	# join all pages text into single string variable
	text_temp = " ".join(text_lst)
	return text + text_temp

def text_to_speech(text, file_name):
	# create a speech objeect
    speech = gTTS(text = text, slow = False)
    audio_file = f'{file_name}.mp3'
    # saving audio to disk
    speech.save(audio_file)
    return audio_file

def stylize():
    
    #Footer vanish
    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)

    #Hamburger menu vanish
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

stylize()

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center ; color: black;'>Research : Audiofy 🎶</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center ; color: black;'><strong>by M. Sreenidhi Iyengar & M. Harika</strong></h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a Pdf file", type=["pdf"])

text = audio_file_name = None

if uploaded_file is not None:
	text = pypdf2(uploaded_file)
	audio_file_name = text_to_speech(text, uploaded_file.name)

	audio_file = open(audio_file_name, 'rb')
	audio_bytes = audio_file.read()
	st.audio(audio_bytes, format='audio/mp3')
	audio_file.close()
	os.remove(audio_file_name)
