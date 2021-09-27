import streamlit as st
import homography
import stitching
import introduction
import interactive_homography
import hough_lines
import conclusione

PAGES = {
	"Introduzione": introduction,
    "Stitching": stitching,
    "Omografia Manuale": homography,
    "Omografia interattiva": interactive_homography,
    "Linee di Hough": hough_lines,
    'Conclusioni': conclusione
}
st.set_page_config(page_title='Basketball Detection', page_icon=':basketball:', layout='centered', initial_sidebar_state='auto')
st.sidebar.title('Navigazione')
selection = st.sidebar.radio("vai", list(PAGES.keys()))
page = PAGES[selection]
page.app()
