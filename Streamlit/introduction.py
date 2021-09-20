import streamlit as st
import numpy as np
import cv2
from constants import PATH_IMGS_EXAMPLE, PATH_VIDEO_EXAMPLE, FRAME_EXTRACTOR, PATH_SCRIPTS
import utils


def app():
    st.title("Introduzione")

    st.subheader("Esempi di video utilizzati")
    col1,col2 = st.columns(2)
   
    video_file_lakers = open(PATH_VIDEO_EXAMPLE + 'lakers.mp4', 'rb') 
    video_bytes_lakers = video_file_lakers.read()
    video_file_oklahoma = open(PATH_VIDEO_EXAMPLE + 'oklahoma.mp4', 'rb') 
    video_bytes_oklahoma = video_file_oklahoma.read()

    col1.video(video_bytes_lakers)
    col2.video(video_bytes_oklahoma)
    
    st.write('''
    Le clip sono state registrate dal videogame NBA2K21 e sono stati estratti dei frame utilizzando uno script python in grado di estrarre un frame per ogni secondo. Di seguito il codice:
    ''')

    my_expander = st.expander(label='CLick to show code')
    with my_expander:
      st.code(FRAME_EXTRACTOR, language= 'python')
      st.markdown(utils.get_binary_file_downloader_html(PATH_SCRIPTS + 'frame_extractor.py', 'Code'), unsafe_allow_html=True)

    
    real = cv2.imread(PATH_IMGS_EXAMPLE + "/real.jpg")
    game = cv2.imread(PATH_IMGS_EXAMPLE + "/game.jpg")
    real1 = cv2.imread(PATH_IMGS_EXAMPLE + "/real1.jpg")
    game1 = cv2.imread(PATH_IMGS_EXAMPLE + "/game1.jpg")
    real2 = cv2.imread(PATH_IMGS_EXAMPLE + "/real2.png")
    game2 = cv2.imread(PATH_IMGS_EXAMPLE + "/game2.jpg")

    st.image(real, channels='BGR', caption="TD Garden (Boston)")
    st.image(real1, channels= 'BGR', caption="Staples Center - Lakers (Los Angeles)")
    st.image(real2, channels='BGR', caption="Mediolanum Forum (Milano)")
    st.image(game, channels= 'BGR', caption="Staples Center - Lakers (Los Angeles) da NBA2K21")
    st.image(game1, channels='BGR', caption="Chesapeake Energy Arena (Oklahoma) da NBA2K21")
    st.image(game2, channels= 'BGR', caption="Scotiabank Arena (Toronto) da NBA2K21")

    st.markdown("---")
    st.write(
    '''Risulta chiara, dagli esempi sopra presentati, la presenza di watermark.
       Questi ultimi sono stati rimossi in una fase di pre-elaborazione delle immagini per garantire una migliore riuscita dello stitching.
       (VALUTARE SE LASCIARE O MENO)
    ''')

    watermark = cv2.imread(PATH_IMGS_EXAMPLE + "/watermark.jpg")
    nowatermark = cv2.imread(PATH_IMGS_EXAMPLE + "/nowatermark.jpg")

    st.image(watermark, channels='BGR', caption="Immagine con watermark")
    st.image(nowatermark, channels= 'BGR', caption="Immagine senza watermark")