import streamlit as st
from gtts import gTTS

text=st.text_input("Choose a text to speak out:")
speak=st.button("Speak it out!")

if text and speak:
    speech = gTTS(text=text)
    speech.save("audio.mp3")
    st.audio("audio.mp3", format="audio/mp3")
