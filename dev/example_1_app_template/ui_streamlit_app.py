"""
Goal of this file:
given an app that has a simple text-based interface, we want to create a Streamlit interface for it
app will have .invoke() method that takes a string and returns a string
"""
from app import App

import streamlit as st

app = App()

def main():
    input_str = st.text_input("Enter your input")
    output_str = app.invoke(input_str)
    st.write(output_str)

if __name__ == '__main__':
    main()
# Compare this snippet from dev/example_1_app_template/ui_telegram_bot.py:
