import streamlit as st
from temiturkishModel3 import temi_main
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import tempfile
import io
import os


def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="tr-TR")
    return text


def main():
    st.title("OSTIMTECH TEMI")
    st.sidebar.image("logo.png", use_column_width=True)
    recorder_result = audio_recorder(key="ar")

    if recorder_result:
        # recorder_result ile döndürülen veriyi bir geçici dosyaya yaz
        try:
            # Tempfile kullanarak geçici dosya oluştur
            tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            tmpfile.write(recorder_result)
            tmpfile.close()  # Dosyayı yazdıktan sonra kapat

            text = convert_audio_to_text(tmpfile.name)
            st.write("Sorunuz: ", text)

            answer, speech_file_path = temi_main(text)
            st.write("Cevap: ", answer)

            st.audio(speech_file_path)
        finally:
            # İşlem tamamlandıktan sonra geçici dosyayı sil
            if tmpfile:
                os.remove(tmpfile.name)


if __name__ == "__main__":
    main()
