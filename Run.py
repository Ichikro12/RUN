import subprocess
import streamlit as st

st.write('Click to start innovarium module')
if st.button('Start'):
    # Run Streamlit app
    process = subprocess.Popen(['streamlit', 'run', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for Streamlit app to start
    process.stdout.readline()

    # Wait for the Streamlit app to finish
    process.wait()
