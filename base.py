import streamlit as st
import textwrap
import google.generativeai as genai

# Function to convert text to Markdown format
def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Configure Google GenerativeAI with your API key
genai.configure(api_key="AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms")

# Streamlit app title and description
st.write("""
# Ask Steve a question about AML compliance:
""")

# Streamlit form for user input
with st.form(key='user_question_form'):
    question = st.text_input("Enter your question for Steve:")
    submit_button = st.form_submit_button(label='Submit')

# Check if the submit button is pressed and if there's a question entered
if submit_button and question:
    
    # Instantiate Generative Model
    model = genai.GenerativeModel(model_name='gemini-pro')

    # Generate content using the combined prompt
    # Assuming that the correct method is called here as per the API's documentation
    response = model.generate_content(question)

    # Display generated content
    st.write(to_markdown(response.text))
