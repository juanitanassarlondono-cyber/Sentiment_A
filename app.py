from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from deep_translator import GoogleTranslator

# Cambio visual: configuración general de página
st.set_page_config(
    page_title="Análisis emocional de texto",
    page_icon="💬",
    layout="centered"
)

# Cambio visual: colores y fuentes con CSS personalizado
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #F7EDE2 0%, #F5CAC3 45%, #D8E2DC 100%);
        color: #2F2F2F;
        font-family: 'Trebuchet MS', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #6D4C41;
    }

    .stTextInput label, .stExpander, .stSidebar {
        font-family: 'Trebuchet MS', sans-serif;
    }

    section[data-testid="stSidebar"] {
        background-color: #B0E0E6;
    }

    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.65);
        border-radius: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Cambio de palabras: título principal
st.title('Evaluación de Sentimiento')

# Cambio de imagen: emoticones.jpg reemplazado por emociones.jpg
image = Image.open('emociones.jpg')
st.image(image)

# Cambio de palabras: descripción principal
st.subheader("Ingresa en el campo de texto la frase que quieres evaluar")


with st.sidebar:
               # Cambio de palabras: título del panel lateral
               st.subheader("Tono emocional y subjetividad")
               ("""
                Polaridad: Señala si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor va desde -1, que representa un tono muy negativo, hasta 1, que representa un tono muy positivo. 
                El 0 indica una expresión neutral.
                
               Subjetividad: Evalúa qué tanto el contenido refleja opiniones, emociones o creencias frente a información objetiva.
               Su escala va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 

# Cambio de palabras: nombre del expander
with st.expander('Evaluar texto'):
    text = st.text_input('Escribe tu frase aquí: ')
    if text:

       
        trans_text = GoogleTranslator(source="es", target="en").translate(text)
        blob = TextBlob(trans_text)

        # Cambio de palabras: etiquetas visibles de resultados
        st.write('Polaridad: ', round(blob.sentiment.polarity,2))
        st.write('Subjetividad: ', round(blob.sentiment.subjectivity,2))

        x=round(blob.sentiment.polarity,2)
        if x > 0.0 and x <=1.0:
            st.write( 'El sentimiento identificado es positivo 😊')
        elif x >=-1 and x <= 0:
            st.write( 'El sentimiento identificado es negativo 😔')
        else:
            st.write( 'El sentimiento identificado es neutral 😐')
