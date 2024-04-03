import subprocess
import streamlit as st

st.write('Enter the path of the Streamlit app and click to start:')
input_value = st.text_input("Streamlit App Path") # Add a text input for the Streamlit app path

if st.button('Start'):
    if input_value:
        # Run Streamlit app with the provided path
        process = subprocess.Popen(['streamlit', 'run', input_value], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for Streamlit app to start
        process.stdout.readline()

        # Wait for the Streamlit app to finish
        process.wait()
    else:
        st.warning("Please provide a valid Streamlit app path.")
