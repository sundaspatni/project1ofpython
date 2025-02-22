#import process

import streamlit as st

st.set_page_config(page_title= "Mindset Challenge project")
st.title("Challenge Mindset AI Project: Web App with Streamlit ")

st.header(" Welcome to Mndset Challenge Journey!")
st.write(" This journey begins with self-awareness, recognizing the limitations of previous thinking, and being open to new strategies. Along the way, individuals face obstacles, but instead of being discouraged, they see these as opportunities to grow and learn.")

#quote about success
st.header(" Today's Challenge Project Quote")
st.write("Success is not the destination, but the courage to keep moving forward.")

st.header(" What's your Challenge Today?")
user_input = st.text_input("Describe challenge you are facing:")

#condition
if user_input:
    st.success(f" you are facing: {user_input}. keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

    #reflection
st.header(" Reflect on your Learning")
reflection = st.text_area("write your output here:")

if reflection:
    st.success(f" Great Insight! your outcome {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

#achievements

st.header(" Celebrate your wins!")
acheivment = st.txt_input("Share something you've recently accomplished!")

if acheivment:
    st.success(f"  Amazing! you achieved: {acheivment}")
else:
    st.info("Big or Small, every achievement counts! share one now") 

    #footer
    st.write("---")
    st.write(" Embrace the challenge, for every step you take toward growth brings you closer to becoming the best version of yourself.")   
    st.write(" Created by Sundas Dilawer")





