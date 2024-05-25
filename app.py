# Kyle Billones BSCS 3B - AI 
# This is a simple Streamlit app that uses the Google Generative AI API to create an event plan.

#Import Google API Key 
from dotenv import load_dotenv
load_dotenv()

#Import the necessary libraries
import streamlit as st
import os
import google.generativeai as genai

# Set the API key
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini model and get respones
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

def main():

    # Streamlit User Interface styling  
    st.markdown("""
        <style>
        .reportview-container {
            flex-direction: row;
        }
        .sidebar .sidebar-content {
            background-color: darkblue;
            color: white;
        }
        .reportview-container .main .block-container {
            width: 70%;
            float: right;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Streamlit Sidebar Header 
    st.sidebar.title('📝 EventBOT')
    st.sidebar.write('Tired of planning and structuring events? Let EventBOT help you!')
    st.sidebar.write('')

    # Streamlit Sidebar Inputs (Guide questions for the prompt)
    event_input = st.sidebar.text_input("What is the name of your event?")
    date_input = st.sidebar.text_input("When will it be held? (Month-Day-Year)")
    venue_input = st.sidebar.text_input("Where is the venue of the said event?")
    participant_input = st.sidebar.text_input("Who are the target participants? (Separate using comma)")
    activities_input = st.sidebar.text_input("What are the expected activities in the said event (Separate using comma)?")
    st.sidebar.write('')
    st.sidebar.write('')

    # Streamlit Additional Model Instructions (Multi-Level Prompting)
    ask_question = "Make me an event plan, used the following as your input." + "Event Name:"+ event_input + ". Date:" + date_input + ". Venue " + venue_input + " Participants: " + participant_input + " Activities: " + activities_input + ""
    instruction_1= "Structure it this order, Event name, date, venue, participants, overview (in paragraph form), program flow, objectives, needed materials or resources to prepare (provide price in PHP if possible, add a total too, present in a table), conclusion."
    instruction_2= "Layout it well and make it presentable."
    instruction_3 = "Make event rationale in a paragraph form"
    instruction_4 = "Add short description of the event objectives"
    instruction_5 = "Write a program flow of the event. (Time - activity description - person in charge (if applicable), present in a table"
    input = " "+ask_question+" "+ instruction_1+" "+instruction_2+" "+instruction_3+" "+instruction_4+" "+instruction_5+" "

    # Streamlit Submit Button and Response Display (Event Plan Design)
    submit_button = st.sidebar.button('Submit')
    if submit_button:
        response=get_gemini_response(input)
        st.subheader("Hi, I'm EventBOT! Here's the event design I made for you.")
        st.write(response)

if __name__ == "__main__":
    main()