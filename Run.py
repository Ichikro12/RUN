import streamlit as st
import subprocess

def start_streamlit():
    process = subprocess.Popen(['streamlit', 'run', 'iitbombay-main/pythonproject1/main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()

def main():
    st.title("Streamlit App Starter")

    # Function to start the Streamlit app
    def start_app():
        start_streamlit()

    # Button to start the app
    if st.button("Start App"):
        start_app()

if __name__ == "__main__":
    main()
