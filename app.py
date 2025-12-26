import streamlit as st

# Seitentitel
st.title("Hello World! 👋")

# Einfacher Text
st.write("Willkommen zu meiner ersten Streamlit-App!")

# Ein bisschen mehr Inhalt
st.header("Das ist eine Überschrift")
st.text("Das ist ein einfacher Text.")

# Ein Button
if st.button("Klick mich!"):
    st.balloons()
    st.success("Hallo Welt! 🎉")
